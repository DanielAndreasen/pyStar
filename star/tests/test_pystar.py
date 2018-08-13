import pytest

from enums.evolutionary_stage import Stage
from enums.spectral_type import SpectralType
from pyStar import getStage, Star

from colour import Colour
from seismology import Seismology
from spectroscopy import Spectroscopy
from calibrations import Calibrations


@pytest.mark.parametrize('spectral, expected', [
    (SpectralType.G8V, Stage.DWARF),
    (SpectralType.G8III, Stage.GIANT),
    (SpectralType.G8I, Stage.SUPERGIANT),
    (None, None)
])
def test_getStage(spectral, expected):
    stage = getStage(spectral)
    assert stage == expected


def test_star_simple():
    s = Star('Sun')

    assert isinstance(s, Star)
    assert s.spectral == None
    assert s.stage == None
    assert s.colourInformation == False
    assert s.seismicInformation == False
    assert s.spectroscopicInformation == False

    assert 'Sun' in repr(s)
    assert 'Evolutionary stage' not in repr(s)
    assert 'Spectral type' not in repr(s)


def test_add_stars():
    s1 = Star('Good twin')
    s2 = Star('Evil twin')
    with pytest.raises(ValueError):
        s1 + s2


def test_star_complete_flow():
    s = Star('Sun', SpectralType.G2V)
    assert s.spectral == SpectralType.G2V
    assert s.stage == Stage.DWARF

    assert 'Colour' not in repr(s)
    assert 'Seismology' not in repr(s)
    assert 'Spectroscopy' not in repr(s)
    assert 'Calibration' not in repr(s)

    s.getSpectroscopicInformation([3000, 7000, 9000], [1, 0.95, 0.84])
    assert 'Spectroscopy' in repr(s)
    assert isinstance(s.spectroscopic, Spectroscopy)

    s.getSeismicInformation(3.05, 134.9, 5777)
    assert 'Seismology' in repr(s)
    assert isinstance(s.seismic, Seismology)

    spec = s.spectroscopic
    s.getColourInformation(feh=spec.feh, logg=spec.logg, B=1.3, V=0.43)
    assert 'Colour' in repr(s)
    assert isinstance(s.colour, Colour)

    s.getCalibration(spec.Teff, spec.logg, spec.feh)
    assert 'Calibration' in repr(s)
    assert isinstance(s.calibration, Calibrations)


@pytest.mark.parametrize('Teff, logg, feh', [
    (None, 1, 1),
    (1, None, 1),
    (1, 1, None)
])
def test_bad_calibration_parameters(Teff, logg, feh):
    s = Star('Test')
    with pytest.raises(ValueError):
        s.getCalibration(Teff, logg, feh)
