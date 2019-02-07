from vector import Vector
from ctypes import cdll, Structure, c_double, POINTER
from dpcontracts import ensure, require


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

    def set_x(self, x):
        self.set_x_(self.c_vector_pointer, float(x))

    def set_y(self, y):
        self.set_x_(self.c_vector_pointer, float(y))

    def get_x(self):
        return self.get_x_(self.c_vector_pointer)

    def get_y(self):
        return self.get_y_(self.c_vector_pointer)

    x = property(get_x, set_x)
    y = property(get_y, set_y)
