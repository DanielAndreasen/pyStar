from dataclasses import dataclass
import specML
from specML import Data, Model, Minimizer
from spectrum_overload import Spectrum
import numpy as np
from scipy.interpolate import interp1d

from star.myTypes import listLikeType
from star.enums.units import Wavelength
from star.enums.range import Range
from star.validators import val_spectroscopy


@dataclass
class Spectroscopy:
    wavelength: listLikeType
    flux: listLikeType
    unit: Wavelength = Wavelength.AA
    interpolate: bool = False
    verbose: bool = False

    def __post_init__(self):
        self.wavelength = np.asarray(self.wavelength)
        self.flux = np.asarray(self.flux)
        val_spectroscopy.check_input(self.wavelength, self.flux, self.unit)

        if self.unit != Wavelength.AA:
            print('Converting the wavelength to Angstrom')
            self.wavelength = self.wavelength * self.unit.value['conversion']
            if self.unit == Wavelength.ICM:
                self.wavelength = self.wavelength[::-1]
                self.flux = self.flux[::-1]
            self.unit = Wavelength.AA
        self.spectrum: Spectrum = Spectrum(self.flux, self.wavelength)

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
        self.feh: float = 0.82
        self.vmicro: float = 0.85
        self.vmacro: float = 2.43
        self.vsini: float = 4.21

    def getMLparams(self,
                    model: Model,
                    interpolate: bool=False) -> listLikeType:
        self.interpolate = interpolate
        modelWavelength = model.data.get_wavelength()
        if self.interpolate:
            self._interpolate(modelWavelength)

        val_spectroscopy.check_MLmodel(modelWavelength, self.wavelength)

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

    def normalize(self, method='scalar', degree=None, **kwargs):
        self.spectrum = self.spectrum.normalize(method, degree, **kwargs)
        self.wavelength = self.spectrum.xaxis
        self.flux = self.spectrum.flux

    def _get_vmicro(self) -> float:
        if self.logg >= 3.95:  # Dwarfs Tsantaki+ 2013
            return 6.932 * self.Teff * (10 ** (-4)) - 0.348 * self.logg - 1.437
        else:  # Giants Adibekyan+ 2015
            return 2.72 - 0.457 * self.logg + 0.072 * self.feh

    def _get_vmacro(self) -> float:
        if self.logg > 3.9:  # Dwarfs
            T = self.Teff - 5777
            g = self.logg - 4.44
            c = np.array([3.21, 2.33 * 10**(-3), 2.00 * 10**(-6), -2.00])
            p = np.array([1, T, T**2, g])
            return np.dot(c, p)
        # For subgiants and giants: Hekker & Melendez 2007
        elif 2.9 <= self.logg <= 3.9:  # Subgiants
            return -8.426 + (0.00241 * self.Teff)
        elif 1.5 <= self.logg < 2.9:  # Giants
            return -3.953 + (0.00195 * self.Teff)
        else:  # Bright giants
            return -0.214 + (0.00158 * self.Teff)

    def _interpolate(self, wavelength):
        f = interp1d(self.wavelength, self.flux)
        self.flux = f(wavelength)
        self.wavelength = wavelength


def example():  # pragma: no cover
    from pkg_resources import resource_filename
    fname = resource_filename('star', '/data/spec_ml_sample.hdf')
    data = Data(fname, scale=False, with_quadratic_terms=False)
    model = specML.get_model(data)
    wavelength = data.get_wavelength()
    flux = data.y.sample(1).values[0]

    s = Spectroscopy(wavelength, flux, Wavelength.AA, verbose=True)
    p = s.getMLparams(model)
    print('Parameters: ', p)
    s.minimizer.plot()


if __name__ == '__main__':
    example()
