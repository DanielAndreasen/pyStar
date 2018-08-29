import os
from dataclasses import dataclass
from typing import Tuple

from isochrones.starfit import starfit

from star.validators import val_isochrone


@dataclass
class Isochrone:
    teff: Tuple[int, int]
    logg: Tuple[float, float]
    feh: Tuple[float, float]
    verbose: bool = False

    def __post_init__(self):
        print('checking...')
        val_isochrone.check_input(self.teff, self.logg, self.feh)
        val_isochrone.check_ranges(self.teff, self.logg, self.feh)

    def __repr__(self) -> str:
        if hasattr(self, 'age'):
            info: str = f'\nmass: {self.mass}({self.masserr})Msun\n'
            info += f'radius: {self.radius}({self.radiuserr})Rsun\n'
            info += f'age: {self.age}({self.ageerr})Gyr'
            return info
        return 'Nothing calculated yet. Use "Isochrone.getAll()"'

    def getAll(self):
        self._createIni()
        kwargs = self._createKwargs()
        self.starModel, _ = starfit('.', **kwargs)
        self._clean()

        self.samples = self.starModel.samples
        resume = self.samples.describe()

        self.mass = round(resume.at['mean', 'mass_0_0'], 2)
        self.masserr = round(resume.at['std', 'mass_0_0'], 2)
        self.radius = round(resume.at['mean', 'radius_0_0'], 2)
        self.radiuserr = round(resume.at['std', 'radius_0_0'], 2)
        self.age = round(resume.at['mean', 'age_0_0'], 2)
        self.ageerr = round(resume.at['std', 'age_0_0'], 2)

    def _createIni(self):
        with open('star.ini', 'w') as f:
            f.write(f'Teff = {self.teff[0]}, {self.teff[1]}\n')
            f.write(f'logg = {self.logg[0]}, {self.logg[1]}\n')
            f.write(f'feh = {self.feh[0]}, {self.feh[1]}\n')
            f.write('V = 10.0, 0.05\n')

    def _clean(self):
        files = ('star.ini', 'starfit.log',
                 'mist_corner_single_observed.png',
                 'mist_corner_single_physical.png',
                 'mist_starmodel_single.h5',
                 'mist_corner_single.h5')
        for file in files:
            try:
                os.remove(file)
            except FileNotFoundError:
                pass

    def _createKwargs(self) -> dict:
        return dict(models='mist', use_emcee=True, verbose=self.verbose)


if __name__ == '__main__':

    teff = (5777, -50)
    logg = (4.44, 0.03)
    feh = (0.00, 0.02)
    iso = Isochrone(teff, logg, feh)
    iso.getAll()
    print(iso)
