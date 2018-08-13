import pytest

from enums.evolutionary_stage import Stage


def test_stages():
    assert isinstance(Stage.PMS, Stage)
    assert isinstance(Stage.PMS.value, str)

    assert Stage.PMS.value == 'PRE MS'
    assert Stage.DWARF.value == 'DWARF'
    assert Stage.SUBGIANT.value == 'SUBGIANT'
    assert Stage.GIANT.value == 'GIANT'
    assert Stage.SUPERGIANT.value == 'SUPERGIANT'
    assert Stage.WD.value == 'WHITE DWARF'
    assert Stage.NS.value == 'NEUTRON STAR'
    assert Stage.BH.value == 'BLACK HOLE'


def test_no_stage():
    with pytest.raises(AttributeError):
        Stage.TEST
