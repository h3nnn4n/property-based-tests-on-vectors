import numpy as np
from math import cos, sin, pi, atan2, isnan
from vector import Vector
from random import uniform
from dpcontracts import require, ensure


class VectorNumpy(Vector):
    def __init__(self, x=0, y=0):
        self.data = np.asarray([x, y])

    @require("`x` must be a valid C long",
             lambda args: valid_range(args[1]))
    @require("`x` must be a valid number",
             lambda args: is_valid_number(args[1]))
    def set_x(self, x):
        self.data[0] = x

    @require("`y` must be a valid C long",
             lambda args: valid_range(args[1]))
    @require("`y` must be a valid number",
             lambda args: is_valid_number(args[1]))
    def set_y(self, y):
        self.data[1] = y

    def get_x(self):
        return self.data[0]

    def get_y(self):
        return self.data[1]

    @property
    def norm(self):
        return np.sqrt(np.sum(self.data ** 2))

    x = property(get_x, set_x)
    y = property(get_y, set_y)


def is_valid_number(number):
    if isnan(number) or number == float("inf") or number == float("-inf"):
        return False

    return True


def valid_range(number):
    if number > 2**31-1 or number < -2**31-1:
        return False

    return True
