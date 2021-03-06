from star.calibrations import Calibrations
import numpy as np


def test_simple():
    c = Calibrations(5777, 4.438, 0.00)
    m = c.getMass()
    r = c.getRadius()
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


def test_sun():
    c = Calibrations(5777, 4.428, 0.00)
    c.getAll()
    assert round(c.mass) == 1  # Allow for scatter from calibration
    assert round(c.radius) == 1  # Allow for scatter from calibration
