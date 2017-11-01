from libc.stdint cimport uint32_t, uint64_t, int32_t
from libcpp.string cimport string


cdef extern from 'protozero/pbf_reader.hpp' namespace 'protozero':
    cdef cppclass data_view:
        data_view()


cdef extern from 'vtzero/geometry.hpp' namespace 'vtzero':
    ctypedef struct point:
        int32_t x
        int32_t y


cdef extern from 'vtzero/feature.hpp' namespace 'vtzero':
    cdef cppclass layer:
        layer()

    cdef cppclass feature:
        feature()
        feature(const layer* layer, const data_view data)


cdef extern from 'vtzero/types.hpp' namespace 'vtzero':
    cdef cppclass index_value:
        index_value()


cdef extern from 'vtzero/builder.hpp' namespace 'vtzero':
    cdef cppclass layer_builder_impl:
        layer_builder_impl()

    cdef cppclass point_feature_builder:
        point_feature_builder()
        point_feature_builder(layer_builder layer, uint64_t id)
        void add_points(uint32_t count)
        void set_point(const point p)
        void set_point(const int32_t x, const int32_t y)
        void add_property(char* key, char* value)  # Fixme: use template args.
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
