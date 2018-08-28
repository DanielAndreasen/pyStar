INPUT_ERROR = 'Please include spectroscopic informations: ' +\
              'Teff, logg, and [Fe/H]'


def check_calibration_input(spectroscopicInformation, Teff, logg, feh):
    cond1 = not spectroscopicInformation
    cond2 = Teff is None or logg is None or feh is None
    if cond1 and cond2:
        raise ValueError(INPUT_ERROR)
