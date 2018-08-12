import pytest
import numpy as np

from spectroscopy import Spectroscopy


def test_simple():
    wavelength = np.linspace(1, 10, 100)
    flux = np.abs(np.random.random(100))
    s = Spectroscopy(wavelength, flux)

    assert isinstance(s.wavelength, np.ndarray)
    assert isinstance(s.flux, np.ndarray)
    assert repr(s) == 'Nothing calculated yet. Use "Spectroscopy.getAll()"'
    s.getAll()
    assert 'Teff' in repr(s)
    assert hasattr(s, 'Teff')
    assert hasattr(s, 'logg')
    assert hasattr(s, 'feh')
    assert hasattr(s, 'vmicro')
    assert hasattr(s, 'vmacro')
    assert hasattr(s, 'vsini')
