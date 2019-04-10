# python-vtzero

Experimental Python wrapper of [vtzero](https://github.com/mapbox/vtzero) a minimalist vector tile decoder and encoder in C++

## Build 

```bash
$ git clone https://github.com/tilery/python-vtzero
$ cd python-vtzero

# download vendor submodules (protozero, mvt-fixtures, vtzero)
$ make init

# Compile .pyx and build
$ make compile
```

## Install

```bash
$ pip install -e .
```

## Example

A complete example can be found [here](example/__init__.py)

```python
from vtzero.tile import VectorTile, Tile, Layer, Point

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

# Encode mvt
data = tile.serialize()
```