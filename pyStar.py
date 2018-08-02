from colour import Colour
from seismology import Seismology
from spectroscopy import Spectroscopy


class Star:

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string. {} was given'.format(type(name)))
        self.name = name
        self.colourInformation = False
        self.seismicInformation = False
        self.spectroscopicInformation = False

    def __add__(self, other):
        raise ValueError('Can not add together two stars')

    def __repr__(self):
        info = f'Star: {self.name}\n'
        if self.colourInformation:
            info += f'Colour - Teff={self.colour.Teff}K\n'
            info += f'Colour - logg={self.colour.logg}dex\n'
            info += f'Colour - [Fe/H]={self.colour.feh}dex\n'
        if self.seismicInformation:
            info += f'Seismology - density={self.seismic.density}g/cm3\n'
            info += f'Seismology - logg={self.seismic.logg}dex\n'
            info += f'Seismology - mass={self.seismic.mass}Msun\n'
            info += f'Seismology - radius={self.seismic.radius}Rsun\n'
        if self.seismicInformation:
            info += f'Spectroscopy - Teff={self.spectroscopic.Teff}K\n'
            info += f'Spectroscopy - logg={self.spectroscopic.logg}dex\n'
            info += f'Spectroscopy - [Fe/H]={self.spectroscopic.feh}dex\n'
            info += f'Spectroscopy - vmicro={self.spectroscopic.vmicro}km/s\n'
            info += f'Spectroscopy - vmacro={self.spectroscopic.vmacro}km/s\n'
            info += f'Spectroscopy - vsini={self.spectroscopic.vsini}km/s\n'
        return info

    def getColourInformation(self, method='Torres', *args, **kwargs):
        print(f'Calculating colour information from method based on: {method}')
        self.colour = Colour(method, *args, **kwargs)
        self.colour.getAll()
        self.colourInformation = True
        print('Values can be reached through: Star.colour.')

    def getSeismicInformation(self, vmax, deltav, Teff):
        self.seismic = Seismology(vmax, deltav, Teff)
        self.seismic.getAll()
        self.seismicInformation = True
        print('Values can be reached through: Star.seismic.')

    def getSpectroscopicInformation(self, wavelength, flux):
        self.spectroscopic = Spectroscopy(wavelength, flux)
        self.spectroscopic.getAll()
        self.spectroscopicInformation = True
        print('Values can be reached through: Star.spectroscopic.')



s1 = Star('Arcturus')
s1.getSpectroscopicInformation([1, 2, 3], [1, 2, 3])
s1.getColourInformation(method='Torres', feh=s1.spectroscopic.feh, logg=s1.spectroscopic.logg)
s1.getSeismicInformation(2.96, 110.54, 4577)

print(s1)
s2 = Star('Sun')
