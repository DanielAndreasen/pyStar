import numpy as np

from myTypes import listLikeType

class Spectroscopy:
    def __init__(self, wavelength: listLikeType, flux: listLikeType) -> None:
        if len(wavelength) != len(flux):
            raise ValueError('Wavelength and flux must have equal length')

        self.wavelength = np.asarray(wavelength)
        self.flux = np.asarray(flux)

        if len(self.wavelength[self.wavelength <= 0]) or len(self.flux[self.flux < 0]):
            raise ValueError('Wavelength and flux can only contain positive numbers')
        if np.sum(np.diff(self.wavelength) <= 0):
            raise ValueError('Wavelength have to be sorted')

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
        self.Teff = 4536
        self.logg = 3.52
        self.feh = 3.82
        self.vmicro = 0.85
        self.vmacro = 2.43
        self.vsini = 4.21