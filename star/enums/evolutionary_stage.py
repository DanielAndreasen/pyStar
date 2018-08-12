from enum import Enum


class Stage(Enum):
    PMS = 'PRE MS'
    DWARF = 'DWARF'
    SUBGIANT = 'SUBGIANT'
    GIANT = 'GIANT'
    SUPERGIANT = 'SUPERGIANT'
    WD = 'WHITE DWARF'
    NS = 'NEUTRON STAR'
    BH = 'BLACK HOLE'
