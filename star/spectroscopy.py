from dataclasses import dataclass
import numpy as np

from myTypes import listLikeType
from enums.units import Wavelength
from enums.range import Range


@dataclass
class Spectroscopy:
    wavelength: listLikeType
    flux: listLikeType
    unit: Wavelength = Wavelength.AA

    def __post_init__(self):
        self.wavelength = np.asarray(self.wavelength)
        self.flux = np.asarray(self.flux)

        if len(self.wavelength) != len(self.flux):
            raise ValueError('Wavelength and flux must have equal length')
        if not len(self.wavelength):
            raise ValueError('Wavelength and flux must contain data')

        if len(self.wavelength[self.wavelength <= 0]) or len(self.flux[self.flux < 0]):
            raise ValueError('Wavelength and flux can only contain positive numbers')
        if self.unit != Wavelength.ICM:
            if np.sum(np.diff(self.wavelength) <= 0):
                raise ValueError('Wavelength have to be sorted')
        else:
            if np.sum(np.diff(self.wavelength[::-1]) <= 0):
                raise ValueError('Wavelength have to be sorted')

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
