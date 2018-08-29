from star.validators.common import is_number


def check_input(teff, logg, feh):
    for v in [teff, logg, feh]:
        if sum(map(is_number, v)) < 2:
            raise ValueError('Parameters have to be numbers')
        if v[1] < 0:
            raise ValueError('Error on parameter has to be positive')


def check_ranges(teff, logg, feh):
    if teff[0] < 3000 or 10000 < teff[0]:
        raise ValueError('Temperature out of range [3,000; 10,000]')

    if logg[0] < 1 or 5 < logg[0]:
        raise ValueError('logg out of range [1; 5]')

    if feh[0] < -3 or 1.5 < feh[0]:
        raise ValueError('[Fe/H] out of range [-3; 1.5]')
