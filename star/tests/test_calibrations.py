from star.calibrations import Calibrations
import numpy as np


def test_simple():
    c = Calibrations(5777, 4.438, 0.00)
    m = c.getMass()
    r = c.getRadius()
    assert isinstance(c.TeffX, float)
    assert isinstance(c.v, np.ndarray)
    assert isinstance(m, float)
    assert isinstance(r, float)
    assert m >= 0
    assert r >= 0


def test_getAll():
    c = Calibrations(5777, 4.438, 0.00)
    c.getAll()
    assert hasattr(c, 'mass')
    assert hasattr(c, 'radius')
    assert isinstance(c.mass, float)
    assert isinstance(c.radius, float)
