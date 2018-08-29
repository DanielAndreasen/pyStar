def is_number(a):
    try:
        float(a)
        return True
    except ValueError:
        return False
