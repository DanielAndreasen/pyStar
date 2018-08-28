import pytest

from star.seismology import Seismology

vmax0: float = 3.05  # mHz
deltav0: float = 134.9  # µHz
Teff0: int = 5777


def test_simple():
    vmax = 1
    deltav = 200
    Teff = 5000
    s = Seismology(vmax, deltav, Teff)

    assert isinstance(s, Seismology)
    assert isinstance(s.vmax, float)
    assert isinstance(s.deltav, float)
    assert isinstance(s.Teff, float)

    assert s.vmax == 1 / vmax0
    assert s.deltav == deltav / deltav0
    assert s.Teff == Teff / Teff0

    assert repr(s) == 'Nothing calculated yet. Use "Seismology.getAll()"'

    s.getAll()

    assert 'logg' in repr(s)
    assert 'density' in repr(s)

    assert hasattr(s, 'mass')
    assert hasattr(s, 'radius')
    assert hasattr(s, 'logg')
    assert hasattr(s, 'density')

    assert s.mass > 0
    assert s.radius > 0
    assert s.density > 0
    assert s.logg > 0

    assert isinstance(s.mass, float)
    assert isinstance(s.radius, float)
    assert isinstance(s.density, float)
    assert isinstance(s.logg, float)


@pytest.mark.parametrize('vmax, deltav, Teff', [
    (-1, 1, 1),
    (1, -1, 1),
    (1, 1, -1),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 0)
])
def test_negative_and_zero_values(vmax, deltav, Teff):
    with pytest.raises(ValueError):
        Seismology(vmax, deltav, Teff)


@pytest.mark.parametrize('vmax, deltav, Teff', [
    (100, 100, 1000),
    (0.001, 100, 1000),
    (1, 1, 1000),
    (1, 10000, 1000),
    (1, 100, 10),
    (1, 100, 100000)
])
def test_not_in_range(vmax, deltav, Teff):
    with pytest.raises(ValueError):
        Seismology(vmax, deltav, Teff)


def test_getGravity():
    s = Seismology(vmax0, deltav0, Teff0)
    assert not hasattr(s, 'mass')

    s.getGravity()

    assert hasattr(s, 'mass')
    assert hasattr(s, 'radius')
    assert hasattr(s, 'logg')
    assert not hasattr(s, 'density')


def test_getDensity():
    s = Seismology(vmax0, deltav0, Teff0)
    assert not hasattr(s, 'mass')

    s.getDensity()

    assert hasattr(s, 'mass')
    assert hasattr(s, 'radius')
    assert hasattr(s, 'density')
    assert not hasattr(s, 'logg')


def test_sun():
    s = Seismology(vmax0, deltav0, Teff0)
    s.getAll()

    assert s.mass == 1.00
    assert s.radius == 1.00
    assert s.logg == 4.44
    assert s.density == 1.41
