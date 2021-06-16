# cython: language_level=3

from libc.stdint cimport uint32_t, uint64_t, int32_t
from libcpp.string cimport string
from libcpp cimport bool


cdef extern from 'protozero/pbf_reader.hpp' namespace 'protozero':
    cdef cppclass data_view:
        data_view()
        const char* data()


cdef extern from 'vtzero/vector_tile.hpp' namespace 'vtzero':
    cdef cppclass vector_tile:
        vector_tile()
        # vector_tile(const data_view data)
        vector_tile(const string& data)
        bool empty()
        size_t count_layers()
        layer next_layer()
        layer get_layer(size_t index)
        layer get_layer_by_name(const data_view name)
        layer get_layer_by_name(const string& name)
        layer get_layer_by_name(const char* name)


cdef extern from 'vtzero/geometry.hpp' namespace 'vtzero':
    ctypedef struct point:
        int32_t x
        int32_t y
    cdef decode_point_geometry(const geometry geometry, bool strict, geom_handler)


cdef extern from 'vtzero/layer.hpp' namespace 'vtzero':
    cdef cppclass layer:
        layer()
        data_view data()
        data_view name()
        uint32_t version()
        uint32_t extent()
        size_t num_features()
        feature next_feature()


cdef extern from 'vtzero/feature.hpp' namespace 'vtzero':

    cdef cppclass feature:
        feature()
        feature(const layer* layer, const data_view data)
        bool has_id()
        uint64_t id()
        GeomType geometry_type()
        geometry geometry()


cdef extern from 'vtzero/types.hpp' namespace 'vtzero':
    cdef cppclass index_value:
        index_value()

    cdef cppclass geometry:
        geometry()


cdef extern from 'vtzero/types.hpp' namespace 'vtzero::GeomType':
    cdef enum GeomType "vtzero::GeomType":
        UNKNOWN
        POINT
        LINESTRING
        POLYGON


cdef extern from 'vtzero/builder.hpp' namespace 'vtzero':
    cdef cppclass layer_builder_impl:
        layer_builder_impl()

    cdef cppclass point_feature_builder:
        point_feature_builder()
        point_feature_builder(layer_builder layer)
        void add_point(const int32_t x, const int32_t y)
        void add_points(uint32_t count)
        void set_point(const point p)
        void set_point(const int32_t x, const int32_t y)
        void add_property(char* key, char* value)
        void set_id(const uint64_t id)
        void commit()
        void rollback()

    cdef cppclass polygon_feature_builder:
        polygon_feature_builder()
        polygon_feature_builder(layer_builder layer)
        void add_ring(uint32_t count)
        void close_ring()
        void set_point(const point p)
        void set_point(const int32_t x, const int32_t y)
        void add_property(char* key, char* value)
        void set_id(const uint64_t id)
        void commit()
        void rollback()

    cdef cppclass linestring_feature_builder:
        linestring_feature_builder()
        linestring_feature_builder(layer_builder layer)
        void add_linestring(uint32_t count)
        void set_point(const point p)
        void set_point(const int32_t x, const int32_t y)
        void add_property(char* key, char* value)
        void set_id(const uint64_t id)
        void commit()
        void rollback()

    cdef cppclass tile_builder:
        tile_builder()
        layer_builder_impl* add_layer(layer& layer)
        layer_builder_impl* add_layer(const char*, uint32_t version, uint32_t extent)
        string serialize()

    cdef cppclass layer_builder:
        layer_builder()
        layer_builder(tile_builder& tile, char* name)
        void add_feature(const feature& feature)
