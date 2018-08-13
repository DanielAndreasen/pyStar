from enum import Enum


class Range(Enum):
    OPTICAL = {'name': 'Optical', 'low': 4000, 'high': 9000}
    NIR = {'name': 'Near-infrared', 'low': 9000, 'high': 20000}
