import pytest
import numpy as np
import specML

from star.spectroscopy import Spectroscopy
from star.enums.units import Wavelength
from star.enums.range import Range


@pytest.fixture
def data():
    from specML import Data
    return Data('data/spec_ml_sample.hdf',
                scale=False,
                with_quadratic_terms=False)


def test_simple():
    wavelength = np.linspace(4000, 9000, 100)
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


def test_wavelength_not_sorted_icm():
    with pytest.raises(ValueError):
        Spectroscopy([1, 2], [1, 2], Wavelength.ICM)


@pytest.mark.parametrize('w0, unit, expected', [
    (0.0001, Wavelength.MICRON, 10),
    (1, Wavelength.NM, 10),
    (10, Wavelength.AA, 10),
    (100000, Wavelength.ICM, 10)
])
def test_wavelength_unit(w0, unit, expected):
    wavelength = [w0, 1000]
    flux = [1, 2]
    s = Spectroscopy(wavelength, flux, unit)
    if unit != Wavelength.ICM:
        assert s.wavelength[0] == expected
    else:
        assert s.wavelength[-1] == expected
        assert (s.flux == np.array([2, 1])).all()  # Bonus test


@pytest.mark.parametrize('w0, w1, expected', [
    (3999, 9001, Range.OPTICAL),
    (8999, 20001, Range.NIR),
    (100, 200, None)
])
def test_range_optical(w0, w1, expected):
    wavelength = [w0, w1]
    flux = [1, 2]
    s = Spectroscopy(wavelength, flux)
    s.getRange()

    assert s.range == expected


def test_outside_range():
    wavelength = [1, 2]
    flux = [1, 0.99]
    s = Spectroscopy(wavelength, flux)
    with pytest.raises(ValueError):
        s.getAll()


def test_get_ml_parameters(data):
    model = specML.get_model(data=data)
    wavelength = data.get_wavelength()
    flux = data.y.sample(1).values[0]
    s = Spectroscopy(wavelength, flux, Wavelength.AA)
    p = s.getMLparams(model)
    assert len(p) == 6
    assert hasattr(s, 'parameters')
    assert hasattr(s, 'Teff')
    assert hasattr(s, 'logg')
    assert hasattr(s, 'feh')
    assert hasattr(s, 'vmicro')
    assert hasattr(s, 'vmacro')
    assert hasattr(s, 'vsini')
    assert hasattr(s, 'MLmodel')


def test_get_ml_parameters_wrong_length(data):
    model = specML.get_model(data=data)
    s = Spectroscopy([1, 2], [1, 2], Wavelength.AA)
    with pytest.raises(ValueError):
        s.getMLparams(model)


def test_get_ml_parameters_wrong_wavelength(data):
    model = specML.get_model(data=data)
    flux = data.y.sample(1).values[0]
    wavelength = np.linspace(1, 2, len(flux))
    s = Spectroscopy(wavelength, flux, Wavelength.AA)
    with pytest.raises(ValueError):
        s.getMLparams(model)


@pytest.mark.parametrize('logg', [3, 4])
def test_vmicro(logg):
    s = Spectroscopy([1, 2], [1, 2])
    s.Teff = 5777
    s.feh = 0.00
    s.logg = logg
    vmicro = s._get_vmicro()

    assert isinstance(vmicro, float)
    assert vmicro >= 0


@pytest.mark.parametrize('logg', [4, 3, 2, 1])
def test_vmacro(logg):
    s = Spectroscopy([1, 2], [1, 2])
    s.Teff = 5777
    s.feh = 0.00
    s.logg = logg
    vmicro = s._get_vmacro()

    assert isinstance(vmicro, float)
    assert vmicro >= 0


def test_interpolate():
    s = Spectroscopy([1, 2], [0.88, 0.93])
    wavelength = np.asarray([1, 1.5, 2])
    s._interpolate(wavelength)
    assert len(s.flux) == len(wavelength)
    assert (s.flux == np.array([0.88, 0.905, 0.93])).all()


def test_interpolate_flow(data):
    model = specML.get_model(data=data)
    wavelength = data.get_wavelength()
    wavelength = np.append(wavelength[::2], wavelength[-1])
    flux = data.y.sample(1).values[0]
    flux = np.append(flux[::2], flux[-1])

    s = Spectroscopy(wavelength, flux, Wavelength.AA)
    p = s.getMLparams(model, interpolate=True)
    assert len(p) == 6


def test_normalization(data):
    wavelength = data.get_wavelength()
    flux = data.y.sample(1).values[0] + 2

    s = Spectroscopy(wavelength, flux)
    s.normalize()

    assert isinstance(s, Spectroscopy)
    assert np.all(s.wavelength == wavelength)
    assert np.any(s.flux != flux)
