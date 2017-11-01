cimport cvtzero
from libcpp.string cimport string
from libc.stdint cimport uint32_t




cdef class VectorTile:

    UNKNOWN = cvtzero.GeomType.UNKNOWN
    POINT = cvtzero.POINT
    LINESTRING = cvtzero.LINESTRING
    POLYGON = cvtzero.POLYGON

    cdef cvtzero.vector_tile* tile
    cdef string data

    def __cinit__(self, string data):
        # C++ will only create a pointer to the python bytes object
        # so let's keep a reference here to be sure it's not garbage
        # collected during the tile lifetime.
        self.data = data
        self.tile = new cvtzero.vector_tile(self.data)

    def empty(self):
        return self.tile.empty()

    def __len__(self):
        return self.tile.count_layers()

    def __next__(self):
        cdef:
            cvtzero.layer layer = self.tile.next_layer()
            VectorLayer pylayer = VectorLayer()
        pylayer.set_layer(layer)
        return pylayer

    def __getitem__(self, item):
        cdef:
            cvtzero.layer layer
            VectorLayer pylayer = VectorLayer()
        if isinstance(item, int):
            layer = self.tile.get_layer(item)
        else:
            self.tile.get_layer_by_name(<string>item)
        pylayer.set_layer(layer)
        return pylayer

    def __dealloc__(self):
        del self.tile


cdef class VectorLayer:

    cdef cvtzero.layer layer

    cdef set_layer(self, cvtzero.layer layer):
        self.layer = layer

    @property
    def name(self):
        return <string>self.layer.name()

    @property
    def version(self):
        return self.layer.version()

    @property
    def extent(self):
        return self.layer.extent()

    def __len__(self):
        return self.layer.num_features()

    def __next__(self):
        cdef:
            cvtzero.feature feature = self.layer.next_feature()
            VectorFeature pyfeature = VectorFeature()
        pyfeature.set_feature(feature)
        return pyfeature


cdef class VectorFeature:

    cdef cvtzero.feature feature

    cdef set_feature(self, cvtzero.feature feature):
        self.feature = feature

    def has_id(self):
        return self.feature.has_id()

    @property
    def id(self):
        return self.feature.id()

    @property
    def geometry_type(self):
        return self.feature.geometry_type()

#     @property
#     def geometry(self):
#         cdef VectorPoint handler = VectorPoint()
#         cvtzero.decode_point_geometry(self.feature.geometry(), True, handler)
#         return handler.data


# cdef class VectorPoint:

#     cdef cvtzero.point data

#     cdef points_begin(self, uint32_t count):
#         self.data.reserve(count)

#     cdef points_point(self, cvtzero.point point):
#         self.data.push_back(point)

#     cdef points_end(self):
#         pass




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
        self.builder = new cvtzero.point_feature_builder(layer.builder[0])

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
