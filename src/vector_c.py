from vector import Vector
from ctypes import cdll, Structure, c_double, POINTER


class CVector(Structure):
    _fields_ = [('x', c_double), ('y', c_double)]


class Vector_C(Vector):
    def __init__(self, x=0, y=0):
        self.vector_c_lib = cdll.LoadLibrary('vector.dylib')
        lib = self.vector_c_lib

        self.create_new_vector = lib.create_new_vector
        self.create_new_vector.restype = POINTER(CVector)

        self.free_vector = lib.free_vector

        self.set_x_ = lib.set_x
        self.set_x_.argtypes = [POINTER(CVector), c_double]

        self.set_y_ = lib.set_y
        self.set_y_.argtypes = [POINTER(CVector), c_double]

        self.get_x_ = lib.get_x
        self.get_x_.argtypes = [POINTER(CVector)]
        self.get_x_.restype = c_double

        self.get_y_ = lib.get_y
        self.get_y_.argtypes = [POINTER(CVector)]
        self.get_y_.restype = c_double

        self.c_vector_pointer = self.create_new_vector()

        self.x = x
        self.y = y

    @require("x must be -2**31-1 <= x <= 2**31-1",
             lambda args: in_valid_range_for_c_double(args.x))
    def set_x(self, x):
        # print('x = ', x)
        self.set_x_(self.c_vector_pointer, float(x))

    @require("x must be -2**31-1 <= y <= 2**31-1",
             lambda args: in_valid_range_for_c_double(args.y))
    def set_y(self, y):
        # print('y = ', y)
        self.set_y_(self.c_vector_pointer, float(y))

    def get_x(self):
        return self.get_x_(self.c_vector_pointer)

    def get_y(self):
        return self.get_y_(self.c_vector_pointer)

    x = property(get_x, set_x)
    y = property(get_y, set_y)


def vector_in_valid_range_for_c_double(vector, safe_range=2**31-1):
    return in_valid_range_for_c_double(vector.x, safe_range=safe_range) and \
        in_valid_range_for_c_double(vector.y)


def in_valid_range_for_c_double(number, safe_range=2**31-1):
    return -safe_range <= number <= safe_range
