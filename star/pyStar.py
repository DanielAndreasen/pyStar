from typing import Optional

from star.colour import Colour
from star.seismology import Seismology
from star.spectroscopy import Spectroscopy
from star.calibrations import Calibrations
from star.isochrone import Isochrone
from star.enums.evolutionary_stage import Stage
from star.enums.spectral_type import SpectralType
from star.myTypes import listLikeType
from star.validators import val_pystar

import numpy as np
from dataclasses import dataclass


def getStage(spectral: SpectralType) -> Stage:
    if spectral is None:
        return None
    if spectral.value['name'].endswith('V'):
        stage = Stage.DWARF
    elif spectral.value['name'].endswith('III'):
        stage = Stage.GIANT
    elif spectral.value['name'].endswith('I'):
        stage = Stage.SUPERGIANT
    return stage


@dataclass
class Star:
    name: str
    spectral: Optional[SpectralType] = None
    stage: Optional[Stage] = None
    colourInformation: bool = False
    seismicInformation: bool = False
    spectroscopicInformation: bool = False
    calibrationInformation: bool = False
    isochroneInformation: bool = False

    def __post_init__(self):
        self.stage = getStage(self.spectral) if self.stage is None else self.stage

    def __add__(self, other) -> None:
        raise ValueError('Can not add together two stars')

    def __repr__(self) -> str:
        info = '#' * 30 + '\n'
        info += f'## Star: {self.name}\n'
        if self.stage is not None:
            info += f'## Evolutionary stage: {self.stage.value}\n'
        if self.spectral is not None:
            info += f'## Spectral type: {self.spectral.value["name"]}\n'
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
        if self.calibrationInformation:
            info += f'# \n# Calibration - mass={self.calibration.mass}Msun\n'
            info += f'# Calibration - radius={self.calibration.radius}Rsun\n'
        if self.isochroneInformation:
            info += f'# \n# Isochrone - mass={self.isochrone.mass}({self.isochrone.masserr})Msun\n'
            info += f'# Isochrone - radius={self.isochrone.radius}({self.isochrone.radiuserr})Rsun\n'
            info += f'# Isochrone - age={self.isochrone.age}({self.isochrone.ageerr})Gyr\n'
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

    def getCalibration(self, Teff: Optional[int]=None, logg: Optional[float]=None,
                       feh: Optional[float]=None) -> None:
        val_pystar.check_calibration_input(self.spectroscopicInformation,
                                           Teff, logg, feh)
        Teff = self.spectroscopic.Teff if Teff is None else Teff
        logg = self.spectroscopic.logg if logg is None else logg
        feh = self.spectroscopic.feh if feh is None else feh
        self.calibration = Calibrations(Teff, logg, feh)
        self.calibration.getAll()
        self.calibrationInformation = True
        print('Values can be reached through: Star.calibration.')

    def getIsochrone(self, Teff: Optional[int]=None, logg: Optional[float]=None,
                     feh: Optional[float]=None) -> None:
        val_pystar.check_isochrone_input(self.spectroscopicInformation,
                                         Teff, logg, feh)
        Teff = self.spectroscopic.Teff if Teff is None else Teff
        logg = self.spectroscopic.logg if logg is None else logg
        feh = self.spectroscopic.feh if feh is None else feh
        self.isochrone = Isochrone((Teff, 50), (logg, 0.05), (feh, 0.05))
        self.isochrone.getAll()
        self.isochroneInformation = True
        print('Values can be reached through: Star.isochrone')


if __name__ == '__main__':
    s1 = Star('Arcturus', SpectralType.K2III)
    s1.getSpectroscopicInformation(np.array([1, 2, 30000]), np.array([1, 2, 3]))
    s1.getColourInformation(method='Ramirez05', feh=s1.spectroscopic.feh,
                            logg=s1.spectroscopic.logg, B=1.3, V=0.43)
    s1.getSeismicInformation(2.96, 110.54, 4577)
    s1.getCalibration()
    s1.getIsochrone()
    print(s1)

    s2 = Star('Sun', SpectralType.G2V, Stage.BH)
    print(s2)

    s3 = Star('Vega', stage=Stage.WD)
    print(s3)
