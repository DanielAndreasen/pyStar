from dataclasses import dataclass
import specML
from specML import Model, Minimizer
import numpy as np

from star.myTypes import listLikeType
from star.enums.units import Wavelength
from star.enums.range import Range


def _check_input(wavelength: np.ndarray, flux: np.ndarray, unit: Wavelength) -> None:
    if len(wavelength) != len(flux):
        raise ValueError('Wavelength and flux must have equal length')
    if not len(wavelength):
        raise ValueError('Wavelength and flux must contain data')

    if len(wavelength[wavelength <= 0]) or len(flux[flux < 0]):
        raise ValueError('Wavelength and flux can only contain positive numbers')
    if unit != Wavelength.ICM:
        if np.sum(np.diff(wavelength) <= 0):
            raise ValueError('Wavelength have to be sorted')
    else:
        if np.sum(np.diff(wavelength[::-1]) <= 0):
            raise ValueError('Wavelength have to be sorted')


@dataclass
class Spectroscopy:
    wavelength: listLikeType
    flux: listLikeType
    unit: Wavelength = Wavelength.AA
    verbose: bool = False

    def __post_init__(self):
        self.wavelength = np.asarray(self.wavelength)
        self.flux = np.asarray(self.flux)
        _check_input(self.wavelength, self.flux, self.unit)

        if self.unit != Wavelength.AA:
            print('Converting the wavelength to Angstrom')
            self.wavelength = self.wavelength * self.unit.value['conversion']
            if self.unit == Wavelength.ICM:
                self.wavelength = self.wavelength[::-1]
                self.flux = self.flux[::-1]
            self.unit = Wavelength.AA

    def __repr__(self) -> str:
        if hasattr(self, 'Teff'):
            info: str = f'Teff: {self.Teff}K\n'
            info += f'logg: {self.logg}dex\n'
            info += f'[Fe/H]: {self.feh}dex\n'
            info += f'vmicro: {self.vmicro}km/s\n'
            info += f'vmacro: {self.vmacro}km/s\n'
            info += f'vsini: {self.vsini}km/s'
            return info
        return 'Nothing calculated yet. Use "Spectroscopy.getAll()"'

    def getAll(self):
        self.getRange()
        if self.range is None:
            raise ValueError('Wavelength coverage is insufficient.')
        self.Teff: int = 4536
        self.logg: float = 3.52
        self.feh: float = 3.82
        self.vmicro: float = 0.85
        self.vmacro: float = 2.43
        self.vsini: float = 4.21

    def getMLparams(self, model: Model) -> listLikeType:
        self.MLmodel = model
        self.minimizer = Minimizer(self.flux, self.MLmodel)
        res = self.minimizer.minimize()
        if self.verbose:
            print('See results with "Spectroscopy.minimizer.plot()"')
        self.Teff = int(res.x[0])
        self.logg = round(res.x[1], 2)
        self.feh = round(res.x[2], 2)
        self.vmicro = round(self._get_vmicro(), 2)
        self.vmacro = round(self._get_vmacro(), 2)
        self.vsini = 2
        self.parameters = [self.Teff, self.logg, self.feh, self.vmicro,
                           self.vmacro, self.vsini]
        return self.parameters

    def getRange(self):
        w_start, w_end = self.wavelength[0], self.wavelength[-1]
        ranges = Range.__members__
        for key in ranges:
            r = ranges[key]
            if w_start <= r.value['low'] and r.value['high'] <= w_end:
                self.range: Range = r
                break
        else:
            self.range = None

    def _get_vmicro(self) -> float:
        if self.logg >= 3.95:  # Dwarfs Tsantaki+ 2013
            return 6.932 * self.Teff*(10**(-4)) - 0.348*self.logg - 1.437
        else:  # Giants Adibekyan+ 2015
            return 2.72 - 0.457*self.logg + 0.072*self.feh

    def _get_vmacro(self) -> float:
        if self.logg > 3.9:  # Dwarfs
            return 3.21 + (2.33 * (self.Teff - 5777.) * (10**(-3))) + (2.00 * ((self.Teff - 5777.)**2) * (10**(-6))) - (2.00 * (self.logg - 4.44))
        # For subgiants and giants: Hekker & Melendez 2007
        elif 2.9 <= self.logg <= 3.9:  # Subgiants
            return -8.426 + (0.00241*self.Teff)
        elif 1.5 <= self.logg < 2.9:  # Giants
            return -3.953 + (0.00195*self.Teff)
        else:  # Bright giants
            return -0.214 + (0.00158*self.Teff)


if __name__ == '__main__':
    # NOTE: This line is very slow, but only used for testing.
    model = specML.get_model()
    data = model.data
    wavelength = data.get_wavelength()
    flux = data.y.sample(1).values[0]

    s = Spectroscopy(wavelength, flux, Wavelength.AA, verbose=True)
    p = s.getMLparams(model)
    s.minimizer.plot()
