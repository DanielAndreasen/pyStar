import pytest

from star.enums.spectral_type import SpectralType
from star.enums.spectral_type import getSpectralTypeInformation
import numpy as np


def test_simple():
    assert isinstance(SpectralType.O5V, SpectralType)
    assert isinstance(SpectralType.O5V.value, dict)

    spt = SpectralType.G5V
    assert isinstance(spt.value['name'], str)
    assert spt.value['name'] == 'G5V'

    assert isinstance(spt.value['Teff'], int)
    assert spt.value['Teff'] == 5660

    assert isinstance(spt.value['M'], float)
    assert spt.value['M'] == 5.2

    assert isinstance(spt.value['L'], float)
    assert spt.value['L'] == 0.73


def test_infinite_dim():
    spt = SpectralType.L0V

    assert isinstance(spt.value['M'], float)
    assert spt.value['M'] == np.inf


def test_no_spectral_type():
    with pytest.raises(AttributeError):
        SpectralType.TEST


def test_getSpectralTypeInformation():
    sun = SpectralType.G2V
    info = getSpectralTypeInformation(sun)
    assert info == 'Spectral type: G2V - Teff=5800K'
