import numpt as np

a = np.array([1.5689, 1.3787, 0.4243, 1.139, -0.1425, 0.01969, 0.1010])
b = np.array([2.4427, 0.6679, 0.1771, 0.705, -0.21415, 0.02306, 0.04173])


class Calibrations:

    def __init__(self, Teff=None, logg=None, feh=None):
        self.Teff = Teff
        self.logg = logg
        self.feh = feh
        self.TeffX = np.log(Teff) - 4.1
        self.v = np.array([1, self.TeffX, self.TeffX**2, self.TeffX**3,
                              self.logg**2, self.logg**3, self.feh])

    def getMass(self):
        """From Torres+ 2009"""
        return np.dot(self.v, a)

    def getRadius(self):
        """From Torres+ 2009"""
        return np.dot(self.v, b)
