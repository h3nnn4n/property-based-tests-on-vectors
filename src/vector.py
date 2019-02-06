import numpy as np
from math import cos, sin, pi, atan2, sqrt
from random import uniform


class Vector:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self = Vector(self.x + other.x, self.y + other.y)
        return self

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self = Vector(self.x - other.x, self.y - other.y)
        return self

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __imul__(self, other):
        self = Vector(self.x * other, self.y * other)
        return self

    def __str__(self):
        return '(%12.6f %12.6f)' % (self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def normalize(self):
        norm = self.norm

        if norm != 0:
            self.x /= norm
            self.y /= norm

        return self

    @property
    def norm(self):
        if self.x == 0 and self.y == 0:
            return 0

        return sqrt(self.x**2 + self.y**2)

    @property
    def heading(self):
        return atan2(self.y, self.x)

    def dist(self, other):
        return (
            other
            .copy()
            .__sub__(self)
            .norm
        )

    def limit(self, mag):
        if self.norm > mag:
            self.set_mag(mag)

        return self

    def set_mag(self, mag):
        self.normalize()
        self.set(self * mag)
        return self

    def zero(self):
        self.x = 0
        self.y = 0

        return self

    def set(self, other):
        self.x = other.x
        self.y = other.y

        return self

    def from_angle(self, angle, length=1):
        self.x = length * cos(angle)
        self.y = length * sin(angle)

        return self

    def random(self):
        self.x = uniform(-1, 1)
        self.y = uniform(-1, 1)

        return self

    def copy(self):
        return Vector().set(self)

    x = property(get_x, set_x)
    y = property(get_y, set_y)
