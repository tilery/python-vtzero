# python-vtzero

Experimental Python wrapper of [vtzero](https://github.com/mapbox/vtzero) a minimalist vector tile decoder and encoder in C++

[![Status](https://github.com/tilery/python-vtzero/workflows/CI/badge.svg)](https://github.com/tilery/python-vtzero/actions?query=workflow%3ACI)
[![Packaging status](https://badge.fury.io/py/vtzero.svg)](https://badge.fury.io/py/vtzero)


## Requirements

- Python >= 3.5
- gcc/clang++ >= 4.5 (C++11)

## Install

You can install python-vtzero using pip

```bash
$ pip install vtzero
```

or install from source

```bash
$ git clone https://github.com/tilery/python-vtzero
$ cd python-vtzero

# Download vendor submodules (protozero, mvt-fixtures, vtzero)
$ git submodule update --init

# Compile Cython module
$ python setup.py build_ext --inplace
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
