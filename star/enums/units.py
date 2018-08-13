from enum import Enum


class Wavelength(Enum):
    MICRON = {'name': 'micron', 'conversion': 1e5}
    NM = {'name': 'nanometer', 'conversion': 10}
    AA = {'name': 'Angstrom', 'conversion': 1}
    ICM = {'name': 'Inverse cm', 'conversion': 0.0001}
