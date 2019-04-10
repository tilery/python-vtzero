from vtzero.tile import VectorTile, Tile, Layer, Point, Polygon, Linestring

# Create MVT
tile = Tile()

# Add a layer
layer = Layer(tile, b'my_layer')

# Add a point
feature = Point(layer)
feature.add_points(1)
feature.set_point(10, 10)
feature.add_property(b'foo', b'bar')
feature.add_property(b'x', b'y')
feature.commit()

# Add a polygon
feature = Polygon(layer)
feature.add_ring(5)
feature.set_point(0, 0)
feature.set_point(1, 0)
feature.set_point(1, 1)
feature.set_point(0, 1)
feature.close_ring()
feature.commit()

# Add a line
feature = Linestring(layer)
feature.add_linestring(3)
feature.set_point(0, 0)
feature.set_point(1, 1)
feature.set_point(2, 2)
feature.commit()

# Encode mvt
data = tile.serialize()

# Decode MVT and print info
tile = VectorTile(data)
layer = next(tile)
print(f"Layer Name: {layer.name.decode()}")
print(f"MVT version: {layer.version}")
print(f"MVT extent: {layer.extent}")
features = []
while True:
    f = next(layer)
    if f.geometry_type == 0:
        break
    features.append(f)
print(f"Nb Features: {len(features)}")