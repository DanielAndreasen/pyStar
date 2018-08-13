import pytest
from colour import Colour


@pytest.mark.parametrize("c1,v1,c2,v2", [
    ('B', 0.1, 'V', 0.2),
    ('b', 1.3, 'y', 4.0),
    ('Y', 1.3, 'V', 4.0),
    ('V', 1.3, 'S', 4.0),
    ('B2', 1.3, 'V1', 4.0),
    ('B2', 1.3, 'G', 4.0),
    ('RC', 1.3, 'IC', 4.0)
])
def test_colour_correct(c1, v1, c2, v2):
    c = Colour(method='Ramirez05', feh=0, logg=4, **{c1: v1, c2: v2})
    assert isinstance(c, Colour)
    assert c.X == v1-v2
    assert isinstance(c.X, float)
    assert c.colour == f'{c1}-{c2}'
    assert isinstance(c.colour, str)


@pytest.mark.parametrize('logg', [1, 5])
def test_colour_dwarf_and_giant(logg):
    c = Colour(method='Ramirez05', feh=0, logg=logg, B=0, V=0)
    c.getAll()
    assert hasattr(c, 'Teff')


@pytest.mark.parametrize("c1,v1,c2,v2", [
    ('a', 0.1, 'h', 0.2),
    ('b', 1.3, 'i', 4.0),
    ('c', 1.3, 'j', 4.0),
    ('d', 1.3, 'k', 4.0),
    ('e', 1.3, 'l', 4.0),
    ('f', 1.3, 'm', 4.0),
    ('g', 1.3, 'n', 4.0)
])
def test_colour_incorrect(c1, v1, c2, v2):
    with pytest.raises(ValueError):
        c = Colour(method='Ramirez05', feh=0, logg=4, **{c1: v1, c2: v2})


def test_print():
    c = Colour(method='Ramirez05', feh=0, logg=0, B=1, V=2)
    assert repr(c) == 'Nothing calculated yet. Use "Colour.getAll()"'
    c.getAll()
    assert 'Teff' in repr(c)
