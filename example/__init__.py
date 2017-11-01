from vtzero.tile import Tile, Layer, Point

tile = Tile()
points = Layer(tile, b'points')
feature = Point(points, 1)
feature.add_points(1)
feature.set_point(10, 10)
feature.add_property(b'foo', b'bar')
feature.add_property(b'x', b'y')
feature.commit()
data = tile.serialize()
print(data)
