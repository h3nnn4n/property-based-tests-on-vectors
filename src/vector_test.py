import pytest
from vector import Vector
from math import pi
from hypothesis import given, assume, settings
import math
import numpy as np
import hypothesis.strategies as st


eps = 1e-8


@given(x1=st.integers(), y1=st.integers(), x2=st.integers(), y2=st.integers())
def test_add(x1, y1, x2, y2):
    a = Vector(x1, y1)
    b = Vector(x2, y2)

    c = a + b

    assert c.x == a.x + b.x
    assert c.y == a.y + b.y

    assert a.x == x1
    assert a.y == y1

    assert b.x == x2
    assert b.y == y2


@given(x1=st.integers(), y1=st.integers(), x2=st.integers(), y2=st.integers())
def test_sub(x1, y1, x2, y2):
    a = Vector(x1, y1)
    b = Vector(x2, y2)

    c = a - b

    assert c.x == a.x - b.x
    assert c.y == a.y - b.y

    assert a.x == x1
    assert a.y == y1

    assert b.x == x2
    assert b.y == y2


# TODO
@given(x1=st.integers(), y1=st.integers(), x2=st.integers(), y2=st.integers())
def test_iadd(x1, y1, x2, y2):
    a = Vector(x1, y1)
    b = Vector(x2, y2)
    c = a.copy()

    a += b

    assert a.x == c.x + b.x
    assert a.y == c.y + b.y

    a += Vector(1, 1)

    # assert a.x > c.x
    # assert a.y > c.x


# TODO
@given(x1=st.integers(), y1=st.integers(), x2=st.integers(), y2=st.integers())
def test_isub(x1, y1, x2, y2):
    a = Vector(x1, y1)
    b = Vector(x2, y2)
    c = a.copy()

    a -= b

    assert a.x == c.x - b.x
    assert a.y == c.y - b.y

    # a -= Vector(1, 1)

    # assert a.x < c.x
    # assert a.y < c.x


@given(st.integers(), st.integers())
def test_setter(x, y):
    a = Vector()

    assert a.x == 0
    assert a.y == 0

    a.x = x

    assert a.x == x
    assert a.y == 0

    a.y = y

    assert a.x == x
    assert a.y == y

    a.x = 0
    a.y = 0

    assert a.x == 0
    assert a.y == 0


@given(st.integers(), st.integers(), st.integers())
def test_mul(x, y, z):
    a = Vector(x, y)
    a = a * z

    assert a.x == x * z
    assert a.y == y * z


# TODO
def test_imul():
    a = Vector(1, 1)
    a *= 10

    assert a.x == 10
    assert a.y == 10


@given(st.integers(), st.integers())
def test_norm(x, y):
    a = Vector(x, y)
    norm = a.norm

    assert norm == math.sqrt(a.x**2 + a.y**2)


@given(st.integers(), st.integers())
def test_normalize(x, y):
    assume(x != 0)
    assume(y != 0)

    a = Vector(x, y)
    a.normalize()

    assert abs(a.norm - 1) < eps


@given(st.integers(), st.integers())
def test_zero(x, y):
    a = Vector(x, y)
    a.zero()

    assert a.x == 0
    assert a.y == 0


@settings(max_examples=200)
@given(st.integers(), st.integers(), st.lists(st.integers(min_value=1, max_value=37405339)))
def test_set_mag(x, y, mags):
    assume(x != 0)
    assume(y != 0)
    assume(mags)

    a = Vector(x, y)

    for mag in mags:
        a.set_mag(mag)
        assert abs(a.norm - abs(mag)) < eps


@settings(max_examples=200)
@given(st.integers(), st.integers(), st.lists(st.integers(min_value=0, max_value=37405339).filter(lambda x: x != 0)))
def test_limit(x, y, limits):
    assume(x != 0)
    assume(y != 0)
    assume(limits)

    a = Vector(x, y)

    for limit in limits:
        a.limit(limit)
        assert abs(a.norm - abs(limit)) < eps or a.norm < abs(limit)


@given(st.lists(st.integers(), min_size=4, max_size=4))
def test_set(values):
    x1, x2, y1, y2 = values

    a = Vector(x1, y1)
    b = Vector(x2, y2)
    a.set(b)

    assert a.x == b.x
    assert a.y == b.y

    assert a.x == x2
    assert a.y == y2


@given(x1=st.integers(), y1=st.integers(), x2=st.integers(), y2=st.integers())
def test_dist(x1, y1, x2, y2):
    a = Vector(x1, y1)
    b = Vector(x2, y2)

    assert a.dist(b) == distance(x1, x2, y1, y2)
    assert b.dist(a) == distance(x1, x2, y1, y2)


@given(st.floats(min_value=-pi, max_value=pi, allow_nan=False, allow_infinity=None))
def test_from_angle(angle):
    a = Vector().from_angle(angle)

    assert abs(a.heading - angle) < eps


@given(st.integers(max_value=1e6), st.integers(max_value=1e6), st.integers(min_value=1, max_value=1e6))
def test_heading(x, y, length):
    a = Vector(x, y)

    assert math.atan2(a.y, a.x) == a.heading
    assert -math.pi <= a.heading <= math.pi

    a.set_mag(length)
    b = Vector().from_angle(a.heading, length=a.norm)

    assert abs(a.x - b.x) < eps
    assert abs(a.y - b.y) < eps


# Utils

def distance(x1, x2, y1, y2):
    squared_differences = (x1 - x2)**2 + (y1 - y2)**2
    return math.sqrt(squared_differences)
