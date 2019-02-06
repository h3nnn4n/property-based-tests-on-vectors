import pytest
from vector_numpy import VectorNumpy
from math import pi
from hypothesis import given
import hypothesis.strategies as st


@given(x1=st.integers(), y1=st.integers(), x2=st.integers(), y2=st.integers())
def test_add(x1, y1, x2, y2):
    a = VectorNumpy(x1, y1)
    b = VectorNumpy(x2, y2)

    c = a + b

    assert c.x == a.x + b.x
    assert c.y == a.y + b.y


@given(x1=st.integers(), y1=st.integers(), x2=st.integers(), y2=st.integers())
def test_sub(x1, y1, x2, y2):
    a = VectorNumpy(x1, y1)
    b = VectorNumpy(x2, y2)

    c = a - b

    assert c.x == a.x - b.x
    assert c.y == a.y - b.y


@given(x1=st.integers(), y1=st.integers(), x2=st.integers(), y2=st.integers())
def test_iadd(x1, y1, x2, y2):
    a = VectorNumpy(x1, y1)
    b = VectorNumpy(x2, y2)
    c = a.copy()

    a += b

    assert a.x == c.x + b.x
    assert a.y == c.y + b.y


@given(x1=st.integers(), y1=st.integers(), x2=st.integers(), y2=st.integers())
def test_isub(x1, y1, x2, y2):
    a = VectorNumpy(x1, y1)
    b = VectorNumpy(x2, y2)
    c = a.copy()

    a -= b

    assert a.x == c.x - b.x
    assert a.y == c.y - b.y


def test_setter():
    a = VectorNumpy()

    assert a.x == 0
    assert a.y == 0

    a.x = 1

    assert a.x == 1
    assert a.y == 0

    a.y = 1

    assert a.x == 1
    assert a.y == 1


def test_mul():
    a = VectorNumpy(1, 1)
    a = a * 2

    assert a.x == 2
    assert a.y == 2


def test_imul():
    a = VectorNumpy(1, 1)
    a *= 10

    assert a.x == 10
    assert a.y == 10


def test_norm():
    a = VectorNumpy(3, 4)
    assert a.norm == 5

    a = VectorNumpy()
    assert a.norm == 0


def test_normalize():
    a = VectorNumpy(3, 4)
    a.normalize()

    assert a.norm == 1


def test_zero():
    a = VectorNumpy(1, 1)
    a.zero()

    assert a.x == 0
    assert a.y == 0


def test_set_mag():
    a = VectorNumpy(3, 4)
    a.set_mag(2)
    assert a.norm == 2
    a.set_mag(5)
    assert a.norm == 5
    a.set_mag(1)
    assert a.norm == 1


def test_limit():
    a = VectorNumpy(3, 4)
    assert a.norm == 5

    a.limit(10)
    assert a.norm == 5

    a.limit(3)
    assert a.norm == 3

    a.limit(1)
    assert a.norm == 1


def test_from_angle():
    a = VectorNumpy().from_angle(0)
    assert abs(a.x - 1) < 1e-10
    assert abs(a.y - 0) < 1e-10

    a = VectorNumpy().from_angle(pi / 2)
    assert abs(a.x - 0) < 1e-10
    assert abs(a.y - 1) < 1e-10

    a = VectorNumpy().from_angle(pi)
    assert abs(a.x - -1) < 1e-10
    assert abs(a.y - 0) < 1e-10


def test_set():
    a = VectorNumpy(1, 2)
    b = VectorNumpy(5, 4)
    a.set(b)

    assert a.x == b.x
    assert a.y == b.y


def test_dist():
    a = VectorNumpy(1, 1)
    b = VectorNumpy(1, 2)

    assert a.dist(b) == 1
    assert b.dist(a) == 1

    a = VectorNumpy(2, 3)
    b = VectorNumpy(5, 7)

    assert a.dist(b) == 5
    assert b.dist(a) == 5


def test_heading():
    a = VectorNumpy(1, 0)
    assert a.heading == 0

    a = VectorNumpy(0, 1)
    assert abs(a.heading - pi / 2) < 1e-10

    a = VectorNumpy(-1, 0)
    assert abs(a.heading - pi) < 1e-10
