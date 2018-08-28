def check_input(vmax, deltav, Teff):
    variables = ('vmax', 'deltav', 'Teff')
    values = (vmax, deltav, Teff)
    for variable, value in zip(variables, values):
        if value <= 0:
            raise ValueError(f'{variable} must be positive')

    for variable, value in zip(variables, values):
        if 0.1 > value or value > 10:
            raise ValueError(f'{variable} not in range')
