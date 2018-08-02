import numpy as np
import pandas as pd


class Colour:
    def __init__(self, method, feh, logg, *args, **kwargs):
        self.method = method
        self.feh = feh
        self.logg = logg
        self.colour, self.X = self._getColour(*args, **kwargs)

    def __repr__(self):
        if hasattr(self, 'Teff'):
            info = f'Teff: {self.Teff}({self.eTeff})K\n'
            return info
        return 'Nothing calculated yet. Use "Colour.getAll()"'

    def _getColour(self, *args, **kwargs):
        B = kwargs.pop('B', '')
        V = kwargs.pop('V', '')
        b = kwargs.pop('b', '')
        y = kwargs.pop('y', '')
        Y = kwargs.pop('Y', '')
        S = kwargs.pop('S', '')
        B2 = kwargs.pop('B2', '')
        V1 = kwargs.pop('V1', '')
        G = kwargs.pop('G', '')
        t = kwargs.pop('t', '')
        RC = kwargs.pop('RC', '')
        IC = kwargs.pop('IC', '')
        C4245 = kwargs.pop('C4245', '')
        C4248 = kwargs.pop('C4248', '')
        BT = kwargs.pop('BT', '')
        VT = kwargs.pop('VT', '')
        J2 = kwargs.pop('J2', '')
        H2 = kwargs.pop('H2', '')
        K2 = kwargs.pop('K2', '')
        if B and V:
            return 'B-V', B-V
        if b and y:
            return 'b-y', b-y
        if Y and V:
            return 'Y-V', Y-V
        if V and S:
            return 'V-S', V-S
        if B2 and V1:
            return 'B2-V1', B2-V1
        if B2 and G:
            return 'B2-G', B2-G
        if t:
            return 't', t
        if V and RC:
            return 'V-RC', V-RC
        if V and IC:
            return 'V-IC', V-IC
        if RC and IC:
            return 'RC-IC', RC-IC
        if C4245:
            return 'C(42-45)', C4245
        if C4248:
            return 'C(42-48)', C4248
        if BT and VT:
            return 'BT-VT', BT-VT
        if V and J2:
            return 'V-J2', V-J2
        if V and H2:
            return 'V-H2', V-H2
        if V and K2:
            return 'V-K2', VK2
        if VT and K2:
            return 'VT-K2', VT-K2

    def getAll(self):
        self.Teff = self.calculateTeff()

    def calculateTeff(self):
        theta = self._calcTheta()
        self.Teff = 5040 / theta
        return int(self.Teff)

    def _calcTheta(self):
        a = self._getCoefficients()
        v = np.array([1, self.X, self.X**2, self.X*self.feh, self.feh, self.feh**2])
        return np.dot(a, v)

    def _getCoefficients(self):
        if self.logg < 4.0:
            df = pd.read_csv('colourCoefficientsGiants.csv')
        else:
            df = pd.read_csv('colourCoefficientsDwarfs.csv')
        df = df[df.colour == self.colour]
        self.eTeff = df.eTeff.values[0]
        return df.loc[:, 'a0':'a5']




if __name__ == '__main__':
    c = Colour(method='Ramirez05', feh=0.2, logg=3.3, B=1.2, V=0.57)
    # Or like this:
    # c = Colour(method='Ramirez05', feh=0.2, logg=4.3, **{'B': 1.2, 'V': 0.57})
    c.getAll()
    print(c)
