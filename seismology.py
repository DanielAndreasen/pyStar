import astropy.constants as c
from math import pi, log10

# Constants
vmax0 = 3.05  # mHz
deltav0 = 134.9  #µHz
Teff0 = 5777
M_sun = c.M_sun.to('g').value
R_sun = c.R_sun.to('cm').value
G = c.G.to('cm**3/(g*s**2)').value


class Seismology:

    def __init__(self, vmax, deltav, Teff):
        for variable, value in zip(('vmax', 'deltav', 'Teff'), (vmax, deltav, Teff)):
            if isinstance(value, (int, float)):
                if value <= 0:
                    raise ValueError(f'{variable} must be positive')
            else:
                raise TypeError(f'{variable} must be number-like')

        self.vmax = vmax/vmax0
        self.deltav = deltav/deltav0
        self.Teff = Teff/Teff0

    def __repr__(self):
        if hasattr(self, 'logg') and hasattr(self, 'density'):
            info = f'mass: {self.mass}Msun\n'
            info += f'radius: {self.radius}Rsun\n'
            info += f'logg: {self.logg}dex\n'
            info += f'density: {self.density}g/cm3'
            return info
        return 'Nothing calculated yet. Use "Seismology.getAll()"'

    def getAll(self):
        self.density = self.getDensity()
        self.logg = self.getGravity()
        self.mass = self.getMass()
        self.radius = self.getRadius()

    def getMass(self):
        """From Kjeldsen & Bedding 1995"""
        self.mass = round((self.vmax)**3 * (self.deltav)**(-4) * self.Teff**(3/2), 2)
        return self.mass

    def getRadius(self):
        """From Kjeldsen & Bedding 1995"""
        self.radius = round(self.vmax**3 * self.deltav**(-2) * self.Teff**(3/2), 2)
        return self.radius

    def getDensity(self):
        if not hasattr(self, 'radius'):
            self.radius = self.getRadius()
        if not hasattr(self, 'mass'):
            self.mass = self.getMass()
        self.density = round((self.mass*M_sun) / (4/3*pi*(self.radius*R_sun)**3), 2)
        return self.density

    def getGravity(self):
        if not hasattr(self, 'radius'):
            self.radius = self.getRadius()
        if not hasattr(self, 'mass'):
            self.mass = self.getMass()

        self.g = G*self.mass*M_sun/((self.radius*R_sun)**2)
        self.logg = round(log10(self.g), 2)
        return self.logg


if __name__ == '__main__':
    s = Seismology(3.10, 120.5, 5653)
    s.getAll()
    print(s)
