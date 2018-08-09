import astropy.constants as c
from math import pi, log10

# Constants
vmax0: float = 3.05  # mHz
deltav0: float = 134.9  #µHz
Teff0: int = 5777
M_sun: float = c.M_sun.to('g').value
R_sun: float = c.R_sun.to('cm').value
G: float = c.G.to('cm**3/(g*s**2)').value


class Seismology:

    def __init__(self, vmax: float, deltav: float, Teff: int) -> None:
        for variable, value in zip(('vmax', 'deltav', 'Teff'), (vmax, deltav, Teff)):
            if value <= 0:
                raise ValueError(f'{variable} must be positive')

        self.vmax: float = vmax/vmax0
        self.deltav: float = deltav/deltav0
        self.Teff: float = Teff/Teff0

    def __repr__(self) -> str:
        if hasattr(self, 'logg') and hasattr(self, 'density'):
            info: str = f'mass: {self.mass}Msun\n'
            info += f'radius: {self.radius}Rsun\n'
            info += f'logg: {self.logg}dex\n'
            info += f'density: {self.density}g/cm3'
            return info
        return 'Nothing calculated yet. Use "Seismology.getAll()"'

    def getAll(self):
        self.density: float = self.getDensity()
        self.logg: float = self.getGravity()
        self.mass: float = self.getMass()
        self.radius: float = self.getRadius()

    def getMass(self) -> float:
        """From Kjeldsen & Bedding 1995"""
        self.mass: float = round((self.vmax)**3 * (self.deltav)**(-4) * self.Teff**(3/2), 2)
        return self.mass

    def getRadius(self) -> float:
        """From Kjeldsen & Bedding 1995"""
        self.radius: float = round(self.vmax**3 * self.deltav**(-2) * self.Teff**(3/2), 2)
        return self.radius

    def getDensity(self) -> float:
        if not hasattr(self, 'radius'):
            self.radius = self.getRadius()
        if not hasattr(self, 'mass'):
            self.mass = self.getMass()
        self.density: float = round((self.mass*M_sun) / (4/3*pi*(self.radius*R_sun)**3), 2)
        return self.density

    def getGravity(self) -> float:
        if not hasattr(self, 'radius'):
            self.radius = self.getRadius()
        if not hasattr(self, 'mass'):
            self.mass = self.getMass()

        self.g: float = G*self.mass*M_sun/((self.radius*R_sun)**2)
        self.logg: float = round(log10(self.g), 2)
        return self.logg


if __name__ == '__main__':
    s = Seismology(3.10, 120.5, 5653)
    s.getAll()
    print(s)
