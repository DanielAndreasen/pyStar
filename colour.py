import numpy as np

class Colour:
    def __init__(self, method, feh, logg, *args, **kwargs):
        self.method = method
        self.feh = feh
        self.logg = logg

    def __repr__(self):
        if hasattr(self, 'Teff'):
            info = f'Teff: {self.Teff}K\n'
            return info
        return 'Nothing calculated yet. Use "Colour.getAll()"'

    def getAll(self):
        self.Teff = 1234


    def _calcTheta(self, X):
        a = self._getCoefficients(X)
        v = np.array([1, X, X**2, X*self.feh, self.feh, self.feh**2])
        return np.dot(a, v)

    def _getCoefficients(self, X):
        if self.logg < 4.0:
            return np.array([0.5737, 0.4882, -0.0149, 0.0563, -0.1160, -0.0114])
        else:
            return np.array([0.5002, 0.6440, -0.0690, -0.0230, -0.0566, -0.0170])
