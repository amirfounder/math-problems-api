from random import *


def build_addition_problem():
    n1 = randint(1, 100)
    n2 = randint(1, 100)
    sum = n1 + n2

    p = '{} + {}'.format(n1, n2)
    s = sum

    return p, s


def build_subtraction_problem():
    n1 = randint(1, 100)
    n2 = randint(1, 100)
    difference = n1 - n2

    p = '{} - {}'.format(n1, n2)
    s = difference

    return p, s


def build_multiplication_problem():
    n1 = randint(1, 100)
    n2 = randint(1, 100)
    product = n1 * n2

    p = '{} * {}'.format(n1, n2)
    s = product

    return p, s


def build_division_problem():
    n1 = randint(1, 100)
    n2 = randint(1, 100)
    product = n1 * n2

    p = '{} * {}'.format(n1, n2)
    s = product

    return p, s