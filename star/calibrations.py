from dataclasses import dataclass

import numpy as np

a: np.ndarray = np.array([1.5689, 1.3787, 0.4243, 1.139, -0.1425, 0.01969, 0.1010])
b: np.ndarray = np.array([2.4427, 0.6679, 0.1771, 0.705, -0.21415, 0.02306, 0.04173])


@dataclass
class Calibrations:
    Teff: int
    logg: float
    feh: float

    def __post_init__(self):
        self.TeffX: float = np.log(self.Teff) - 4.1
        self.v: np.ndarray = np.array([1, self.TeffX, self.TeffX**2, self.TeffX**3,
                              self.logg**2, self.logg**3, self.feh])

    def getMass(self) -> float:
        """From Torres+ 2009"""
        return np.dot(self.v, a)

    def getRadius(self) -> float:
        """From Torres+ 2009"""
        return np.dot(self.v, b)

    def getAll(self):
        self.mass = self.getMass()
        self.radius = self.getRadius()


if __name__ == '__main__':
    cal = Calibrations(5777, 4.438, 0.00)
    print(cal.getMass())
    print(cal.getRadius())
