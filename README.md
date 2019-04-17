# python-vtzero

Experimental Python wrapper of [vtzero](https://github.com/mapbox/vtzero) a minimalist vector tile decoder and encoder in C++

[![Travis Build Status](https://travis-ci.org/tilery/python-vtzero.svg?branch=master)](https://travis-ci.org/tilery/python-vtzero)
[![Packaging status](https://badge.fury.io/py/python-vtzero.svg)](https://badge.fury.io/py/python-vtzero)

## Requirements

- Python >= 3.5
- Cython == 0.28
- gcc/clang++ >= 4.5 (C++11)

## Install 

You can install python-vtzero using pip

```bash
$ pip install cython==0.28
$ pip install vtzero
```

or install from source

```bash
$ git clone https://github.com/tilery/python-vtzero
$ cd python-vtzero

# Download vendor submodules (protozero, mvt-fixtures, vtzero)
$ git submodule update --init

$ pip install cython==0.28

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