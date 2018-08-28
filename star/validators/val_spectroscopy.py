import numpy as np

from star.enums.units import Wavelength

SORTED_ERROR = 'Wavelength have to be sorted'
LENGTH_ERROR = 'Wavelength and flux must have equal length'
EMPTY_ERROR = 'Wavelength and flux must contain data'
NEGATIVE_ERROR = 'Wavelength and flux must contain positive numbers'
MODEL_LENGTH_ERROR = 'The length of the wavelength provided is not ' +\
                     'identical to the wavelength from the model.'
MODEL_IDENTITY_ERROR = 'Wavelength for model and provided are not ' +\
                       'identical. Use ' +\
                       'Spectroscopy.getMLparams(model, interpolate=True) ' +\
                       'to fix.'


def check_input(wavelength: np.ndarray,
                flux: np.ndarray,
                unit: Wavelength) -> None:
    _check_length(wavelength, flux)
    _check_wavelength_sorted(wavelength, flux, unit)


def _check_length(wavelength, flux):
    if len(wavelength) != len(flux):
        raise ValueError(LENGTH_ERROR)
    if not len(wavelength):
        raise ValueError(EMPTY_ERROR)


def _check_wavelength_sorted(wavelength, flux, unit):
    if len(wavelength[wavelength <= 0]) or len(flux[flux < 0]):
        raise ValueError(NEGATIVE_ERROR)
    if unit != Wavelength.ICM:
        if np.sum(np.diff(wavelength) <= 0):
            raise ValueError(SORTED_ERROR)
    else:
        if np.sum(np.diff(wavelength[::-1]) <= 0):
            raise ValueError(SORTED_ERROR)


def check_MLmodel(modelWavelength, wavelength):
    if len(modelWavelength) != len(wavelength):
        raise ValueError(MODEL_LENGTH_ERROR)
    if (modelWavelength != wavelength).all():
        raise ValueError(MODEL_IDENTITY_ERROR)
