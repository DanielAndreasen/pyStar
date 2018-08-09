from typing import Union, List, Tuple

from colour import Colour
from seismology import Seismology
from spectroscopy import Spectroscopy
from calibrations import Calibrations
from enums.evolutionary_stage import Stage
from enums.spectral_type import SpectralType

import numpy as np
from myTypes import listLikeType


class Star:

    def __init__(self, name: str, stage: Stage, spectral_type: SpectralType) -> None:
        self.name: str = name
        self.stage: Stage = stage
        self.spectral_type: SpectralType = spectral_type
        self.colourInformation: bool = False
        self.seismicInformation: bool = False
        self.spectroscopicInformation: bool = False

    def __add__(self, other) -> None:
        raise ValueError('Can not add together two stars')

    def __repr__(self) -> str:
        info = '#' * 30 + '\n'
        info += f'## Star: {self.name}\n'
        info += f'## Evolutionary stage: {self.stage.value}\n'
        info += f'## Spectral type: {self.spectral_type.value}\n'
        if self.colourInformation:
            info += f'# \n# Colour - Teff={self.colour.Teff}K\n'
            info += f'# Colour - logg={self.colour.logg}dex\n'
            info += f'# Colour - [Fe/H]={self.colour.feh}dex\n'
        if self.seismicInformation:
            info += f'# \n# Seismology - density={self.seismic.density}g/cm3\n'
            info += f'# Seismology - logg={self.seismic.logg}dex\n'
            info += f'# Seismology - mass={self.seismic.mass}Msun\n'
            info += f'# Seismology - radius={self.seismic.radius}Rsun\n'
        if self.spectroscopicInformation:
            info += f'# \n# Spectroscopy - Teff={self.spectroscopic.Teff}K\n'
            info += f'# Spectroscopy - logg={self.spectroscopic.logg}dex\n'
            info += f'# Spectroscopy - [Fe/H]={self.spectroscopic.feh}dex\n'
            info += f'# Spectroscopy - vmicro={self.spectroscopic.vmicro}km/s\n'
            info += f'# Spectroscopy - vmacro={self.spectroscopic.vmacro}km/s\n'
            info += f'# Spectroscopy - vsini={self.spectroscopic.vsini}km/s\n'
        info += '#' * 30 + '\n'
        return info

    def getColourInformation(self, method: str='Ramirez05', *args, **kwargs):
        print(f'Calculating colour information from method based on: {method}')
        self.colour = Colour(method, *args, **kwargs)
        self.colour.getAll()
        self.colourInformation = True
        print('Values can be reached through: Star.colour.')

    def getSeismicInformation(self, vmax: float, deltav: float, Teff: int) -> None:
        self.seismic = Seismology(vmax, deltav, Teff)
        self.seismic.getAll()
        self.seismicInformation = True
        print('Values can be reached through: Star.seismic.')

    def getSpectroscopicInformation(self, wavelength: listLikeType, flux: listLikeType) -> None:
        self.spectroscopic = Spectroscopy(wavelength, flux)
        self.spectroscopic.getAll()
        self.spectroscopicInformation = True
        print('Values can be reached through: Star.spectroscopic.')


if __name__ == '__main__':
    s1 = Star('Arcturus', Stage.GIANT, SpectralType.K3)
    s1.getSpectroscopicInformation(np.array([1, 2, 3]), np.array([1, 2, 3]))
    s1.getColourInformation(method='Ramirez05', feh=s1.spectroscopic.feh,
                            logg=s1.spectroscopic.logg, B=1.3, V=0.43)
    s1.getSeismicInformation(2.96, 110.54, 4577)

    print(s1)

    s2 = Star('Sun', Stage.DWARF, SpectralType.G4)
    print(s2)