import pytest
from star.isochrone import Isochrone


@pytest.fixture
def isochrone():
    teff = (5777, 50)
    logg = (4.44, 0.03)
    feh = (0.00, 0.02)
    return Isochrone(teff, logg, feh)


def test_flow(isochrone):
    assert isinstance(isochrone, Isochrone)
    assert 'Nothing calculated yet' in repr(isochrone)

    isochrone.getAll()

    assert isinstance(isochrone, Isochrone)
    assert hasattr(isochrone, 'mass')
    assert hasattr(isochrone, 'radius')
    assert hasattr(isochrone, 'age')

    assert isinstance(isochrone.mass, float)
    assert isochrone.mass > 0
    assert isinstance(isochrone.radius, float)
    assert isochrone.radius > 0
    assert isinstance(isochrone.age, float)
    assert isochrone.age > 0

    assert 'age' in repr(isochrone)


@pytest.mark.parametrize('teff, logg, feh', [
    (('test', 50), (4.44, 0.01), (0.00, 0.01)),
    ((5777, 50), ('test', 0.01), (0.00, 0.01)),
    ((5777, 50), (4.44, 0.01), ('test', 0.01)),
    ((5777, 'test'), (4.44, 0.01), (0.00, 0.01)),
    ((5777, 50), (4.44, 'test'), (0.00, 0.01)),
    ((5777, 50), (4.44, 0.01), (0.00, 'test'))
])
def test_nan_input(teff, logg, feh):
    with pytest.raises(ValueError):
        Isochrone(teff, logg, feh)


@pytest.mark.parametrize('teff, logg, feh', [
    ((900, 50), (4.44, 0.01), (0.00, 0.01)),
    ((11000, 50), (4.44, 0.01), (0.00, 0.01)),
    ((5777, 50), (0.9, 0.01), (0.00, 0.01)),
    ((5777, 50), (5.1, 0.01), (0.00, 0.01)),
    ((5777, 50), (4.44, 0.01), (-7.00, 0.01)),
    ((5777, 50), (4.44, 0.01), (2, 0.01))
])
def test_out_of_range(teff, logg, feh):
    with pytest.raises(ValueError):
        Isochrone(teff, logg, feh)


@pytest.mark.parametrize('teff, logg, feh', [
    ((5777, -50), (4.44, 0.01), (0.00, 0.01)),
    ((5777, 50), (4.44, -0.01), (0.00, 0.01)),
    ((5777, 50), (0.9, 0.01), (0.00, -0.01))
])
def test_negative_errors(teff, logg, feh):
    with pytest.raises(ValueError):
        Isochrone(teff, logg, feh)
