from functools import reduce


def factor(n):
    """Function that returns all the factors of the given number"""
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


print(factor(10))
