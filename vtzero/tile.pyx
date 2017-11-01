cimport cvtzero
from libcpp.string cimport string


cdef class Tile:

    cdef cvtzero.tile_builder builder

    def __cinit__(self):
        self.builder = cvtzero.tile_builder()

    def serialize(self):
        return self.builder.serialize()


cdef class Layer:

    cdef cvtzero.layer_builder* builder

    def __cinit__(self, Tile tile, char* name):
        self.builder = new cvtzero.layer_builder(tile.builder, name)


cdef class Point:

    cdef cvtzero.point_feature_builder* builder

    def __cinit__(self, Layer layer, int id):
        self.builder = new cvtzero.point_feature_builder(layer.builder[0], id)

    def add_points(self, count):
        self.builder.add_points(count)

    def set_point(self, x, y):
        self.builder.set_point(x, y)

    def add_property(self, char* key, char* value):
        self.builder.add_property(key, value)

    def commit(self):
        self.builder.commit()

    def rollback(self):
        self.builder.rollback()
