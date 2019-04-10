from vtzero.tile import Tile, Layer, Point, Polygon

tile = Tile()
points = Layer(tile, b'points')
feature = Point(points)
feature.add_points(1)
feature.set_point(10, 10)
feature.add_property(b'foo', b'bar')
feature.add_property(b'x', b'y')
feature.commit()
data = tile.serialize()


tile = Tile()
mvt_layer = Layer(tile, b'polygons')
feature = Polygon(mvt_layer)
feature.add_ring(5)
feature.set_point(0, 0)
feature.set_point(1, 0)
feature.set_point(1, 1)
feature.set_point(0, 1)
feature.close_ring()
feature.commit()
data = tile.serialize()
