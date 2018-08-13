import pytest
import numpy as np

from spectroscopy import Spectroscopy


def test_simple():
    wavelength = np.linspace(1, 10, 100)
    flux = np.abs(np.random.random(100))
    s = Spectroscopy(wavelength, flux)

    assert isinstance(s.wavelength, np.ndarray)
    assert isinstance(s.flux, np.ndarray)
    assert isinstance(s, Spectroscopy)
    assert repr(s) == 'Nothing calculated yet. Use "Spectroscopy.getAll()"'
    s.getAll()
    assert 'Teff' in repr(s)

    assert hasattr(s, 'Teff')
    assert hasattr(s, 'logg')
    assert hasattr(s, 'feh')
    assert hasattr(s, 'vmicro')
    assert hasattr(s, 'vmacro')
    assert hasattr(s, 'vsini')

    assert isinstance(s.Teff, int)
    assert isinstance(s.logg, float)
    assert isinstance(s.feh, float)
    assert isinstance(s.vmicro, float)
    assert isinstance(s.vmacro, float)
    assert isinstance(s.vsini, float)


@pytest.mark.parametrize('wavelength,flux', [
    ([1, 2], [1, 2, 3]),
    ([1, 2, 3], [2, 3]),
    ([], [1])
])
def test_different_length(wavelength, flux):
    with pytest.raises(ValueError):
        Spectroscopy(wavelength, flux)


@pytest.mark.parametrize('wavelength,flux', [
    ([-1, 1, 2], [1, 2, 3]),
    ([1, 2, 3], [-1, 2, 3]),
    ([0, 1, 2], [1, 2, 3])
])
def test_negative_values(wavelength, flux):
    with pytest.raises(ValueError):
        Spectroscopy(wavelength, flux)


def test_empty():
    with pytest.raises(ValueError):
        Spectroscopy([], [])


def test_flux_zero():
    s = Spectroscopy([1], [0])
    assert isinstance(s, Spectroscopy)


def test_wavelength_not_sorted():
    with pytest.raises(ValueError):
        Spectroscopy([2, 1], [42, 21])
