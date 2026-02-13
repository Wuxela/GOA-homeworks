def is_even(n):
    if isinstance(n, float) and n % 1 != 0:
        return False
    return n % 2 == 0