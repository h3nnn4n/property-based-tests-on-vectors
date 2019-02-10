from vector_c import Vector_C
from math import pi
from hypothesis import given, assume
import math
import hypothesis.strategies as st


eps = 1e-8


def integer_on_c_safe_range(safe_range=None):
    if safe_range is None:
        safe_range = 2**28 - 1

    return st.integers(min_value=-safe_range, max_value=safe_range)


@given(x1=integer_on_c_safe_range(),
       y1=integer_on_c_safe_range(),
       x2=integer_on_c_safe_range(),
       y2=integer_on_c_safe_range())
def test_add(x1, y1, x2, y2):
    a = Vector_C(x1, y1)
    b = Vector_C(x2, y2)

    c = a + b

    assert c.x == a.x + b.x
    assert c.y == a.y + b.y

    assert a.x == x1
    assert a.y == y1

    assert b.x == x2
    assert b.y == y2


@given(x1=integer_on_c_safe_range(),
       y1=integer_on_c_safe_range(),
       x2=integer_on_c_safe_range(),
       y2=integer_on_c_safe_range())
def test_sub(x1, y1, x2, y2):
    a = Vector_C(x1, y1)
    b = Vector_C(x2, y2)

    c = a - b

    assert c.x == a.x - b.x
    assert c.y == a.y - b.y

    assert a.x == x1
    assert a.y == y1

    assert b.x == x2
    assert b.y == y2


@given(x1=integer_on_c_safe_range(),
       y1=integer_on_c_safe_range(),
       x2=integer_on_c_safe_range(),
       y2=integer_on_c_safe_range())
def test_iadd(x1, y1, x2, y2):
    a = Vector_C(x1, y1)
    b = Vector_C(x2, y2)
    c = a.copy()

    a += b

    assert a.x == c.x + b.x
    assert a.y == c.y + b.y

    if x1 != 0 and x2 != 0:
        assert a.x != x2

    if y1 != 0 and y2 != 0:
        assert a.y != y2

    a += Vector_C(1, 1)

    assert a.x == c.x + b.x + 1
    assert a.y == c.y + b.y + 1


@given(x1=integer_on_c_safe_range(),
       y1=integer_on_c_safe_range(),
       x2=integer_on_c_safe_range(),
       y2=integer_on_c_safe_range())
def test_isub(x1, y1, x2, y2):
    a = Vector_C(x1, y1)
    b = Vector_C(x2, y2)
    c = a.copy()

    a -= b

    assert a.x == c.x - b.x
    assert a.y == c.y - b.y

    if x1 != 0 and x2 != 0:
        assert a.x != c.x

    if y1 != 0 and y2 != 0:
        assert a.y != c.y

    a -= Vector_C(1, 1)

    assert a.x == c.x - b.x - 1
    assert a.y == c.y - b.y - 1


@given(integer_on_c_safe_range(), integer_on_c_safe_range())
def test_setter(x, y):
    a = Vector_C()

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


@given(integer_on_c_safe_range(), integer_on_c_safe_range())
def test_init(x, y):
    a = Vector_C()

    assert a.x == 0
    assert a.y == 0

    a = Vector_C(x, y)

    assert a.x == x
    assert a.y == y


@given(integer_on_c_safe_range(safe_range=2**15-1),
       integer_on_c_safe_range(safe_range=2**15-1),
       integer_on_c_safe_range(safe_range=2**15-1))
def test_mul(x, y, z):
    a = Vector_C(x, y)
    b = a * z

    assert b.x == x * z
    assert b.y == y * z


@given(integer_on_c_safe_range(safe_range=2**15-1),
       integer_on_c_safe_range(safe_range=2**15-1),
       integer_on_c_safe_range(safe_range=2**15-1))
def test_imul(x, y, z):
    a = Vector_C(x, y)
    a *= z

    assert a.x == x * z
    assert a.y == y * z


@given(integer_on_c_safe_range(), integer_on_c_safe_range())
def test_norm(x, y):
    a = Vector_C(x, y)
    norm = a.norm

    assert norm == math.sqrt(a.x**2 + a.y**2)


@given(integer_on_c_safe_range(), integer_on_c_safe_range())
def test_normalize(x, y):
    assume(x != 0)
    assume(y != 0)

    a = Vector_C(x, y)
    a.normalize()

    assert abs(a.norm - 1) < eps


@given(integer_on_c_safe_range(), integer_on_c_safe_range())
def test_zero(x, y):
    a = Vector_C(x, y)
    a.zero()

    assert a.x == 0
    assert a.y == 0


@given(integer_on_c_safe_range(), integer_on_c_safe_range(),
       st.lists(integer_on_c_safe_range(safe_range=2**25-1)))
def test_set_mag(x, y, mags):
    assume(x != 0)
    assume(y != 0)
    assume(mags)
    assume(0 not in mags)

    a = Vector_C(x, y)

    for mag in mags:
        a.set_mag(mag)
        assert abs(a.norm - abs(mag)) < eps


@given(integer_on_c_safe_range(), integer_on_c_safe_range(),
       st.lists(integer_on_c_safe_range(safe_range=2**26-1)
       .filter(lambda x: x != 0)))
def test_limit(x, y, limits):
    assume(x != 0)
    assume(y != 0)
    assume(limits)

    a = Vector_C(x, y)

    for limit in limits:
        a.limit(limit)
        assert abs(a.norm - abs(limit)) < eps or a.norm < abs(limit)


@given(st.lists(integer_on_c_safe_range(), min_size=4, max_size=4))
def test_set(values):
    x1, x2, y1, y2 = values

    a = Vector_C(x1, y1)
    b = Vector_C(x2, y2)
    a.set(b)

    assert a.x == b.x
    assert a.y == b.y

    assert a.x == x2
    assert a.y == y2


@given(x1=integer_on_c_safe_range(),
       y1=integer_on_c_safe_range(),
       x2=integer_on_c_safe_range(),
       y2=integer_on_c_safe_range())
def test_dist(x1, y1, x2, y2):
    a = Vector_C(x1, y1)
    b = Vector_C(x2, y2)

    eps = 1e-6

    assert a.dist(b) == b.dist(a)
    assert abs(a.dist(b) - distance(x1, x2, y1, y2)) < eps
    assert abs(b.dist(a) - distance(x1, x2, y1, y2)) < eps


@given(st.floats(min_value=-pi, max_value=pi, allow_nan=False,
       allow_infinity=None))
def test_from_angle(angle):
    a = Vector_C().from_angle(angle)

    assert abs(a.heading - angle) < eps


@given(integer_on_c_safe_range(), integer_on_c_safe_range(),
       st.integers(min_value=1, max_value=1e6))
def test_heading(x, y, length):
    a = Vector_C(x, y)

    assert math.atan2(a.y, a.x) == a.heading
    assert -math.pi <= a.heading <= math.pi

    a.set_mag(length)
    b = Vector_C().from_angle(a.heading, length=a.norm)

    assert abs(a.x - b.x) < eps
    assert abs(a.y - b.y) < eps


@given(integer_on_c_safe_range())
def test_random(_):
    a = Vector_C().random()

    assert -1 <= a.x <= 1
    assert -1 <= a.y <= 1


# Utils

def distance(x1, x2, y1, y2):
    squared_differences = (x1 - x2)**2 + (y1 - y2)**2
    return math.sqrt(squared_differences)
