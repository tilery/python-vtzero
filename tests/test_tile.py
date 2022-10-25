from vtzero.tile import Layer, Linestring, Point, Polygon, Tile


def test_point_encoding():
    """Test creation of point feature."""
    tile = Tile()
    points = Layer(tile, b"points")
    feature = Point(points)
    feature.add_points(1)
    feature.set_point(10, 10)
    feature.add_property(b"foo", b"bar")
    feature.add_property(b"x", b"y")
    feature.commit()
    assert (
        tile.serialize()
        == b'\x1a0x\x02\n\x06points(\x80 \x12\r\x18\x01"\x03\t\x14\x14\x12\x04\x00\x00\x01\x01\x1a\x03foo\x1a\x01x"\x05\n\x03bar"\x03\n\x01y'
    )  # noqa


def test_polygon_encoding():
    """Test creation of polygon feature."""
    tile = Tile()
    poly = Layer(tile, b"polygon")
    feature = Polygon(poly)
    feature.add_ring(5)
    feature.set_point(0, 0)
    feature.set_point(10, 0)
    feature.set_point(10, 10)
    feature.set_point(0, 10)
    feature.set_point(0, 0)
    feature.add_property(b"foo", b"bar")
    feature.commit()
    assert (
        tile.serialize()
        == b'\x1a/x\x02\n\x07polygon(\x80 \x12\x13\x18\x03"\x0b\t\x00\x00\x1a\x14\x00\x00\x14\x13\x00\x0f\x12\x02\x00\x00\x1a\x03foo"\x05\n\x03bar'
    )  # noqa


def test_polygon_encoding_close_ring():
    """Test creation of polygon feature with 'close_ring' method."""
    tile = Tile()
    poly = Layer(tile, b"polygon")
    feature = Polygon(poly)
    feature.add_ring(5)
    feature.set_point(0, 0)
    feature.set_point(10, 0)
    feature.set_point(10, 10)
    feature.set_point(0, 10)
    feature.close_ring()
    feature.add_property(b"foo", b"bar")
    feature.commit()
    assert (
        tile.serialize()
        == b'\x1a/x\x02\n\x07polygon(\x80 \x12\x13\x18\x03"\x0b\t\x00\x00\x1a\x14\x00\x00\x14\x13\x00\x0f\x12\x02\x00\x00\x1a\x03foo"\x05\n\x03bar'
    )  # noqa


def test_linestring_encoding():
    """Test creation of linestring feature."""
    tile = Tile()
    line = Layer(tile, b"linestring")
    feature = Linestring(line)
    feature.add_linestring(3)
    feature.set_point(0, 0)
    feature.set_point(10, 10)
    feature.set_point(20, 20)
    feature.add_property(b"foo", b"bar")
    feature.commit()
    assert (
        tile.serialize()
        == b'\x1a/x\x02\n\nlinestring(\x80 \x12\x10\x18\x02"\x08\t\x00\x00\x12\x14\x14\x14\x14\x12\x02\x00\x00\x1a\x03foo"\x05\n\x03bar'
    )  # noqa


def test_set_id_valid():
    """Test set_id method."""
    tile = Tile()
    points = Layer(tile, b"points")
    feature = Point(points)
    feature.set_id(1)
    feature.add_points(1)
    feature.set_point(10, 10)
    feature.add_property(b"foo", b"bar")
    feature.add_property(b"x", b"y")
    feature.commit()
    assert (
        tile.serialize()
        == b'\x1a2x\x02\n\x06points(\x80 \x12\x0f\x18\x01\x08\x01"\x03\t\x14\x14\x12\x04\x00\x00\x01\x01\x1a\x03foo\x1a\x01x"\x05\n\x03bar"\x03\n\x01y'
    )  # noqa

    tile = Tile()
    poly = Layer(tile, b"polygon")
    feature = Polygon(poly)
    feature.set_id(1)
    feature.add_ring(5)
    feature.set_point(0, 0)
    feature.set_point(10, 0)
    feature.set_point(10, 10)
    feature.set_point(0, 10)
    feature.set_point(0, 0)
    feature.commit()
    assert (
        tile.serialize()
        == b'\x1a!x\x02\n\x07polygon(\x80 \x12\x11\x18\x03\x08\x01"\x0b\t\x00\x00\x1a\x14\x00\x00\x14\x13\x00\x0f'
    )  # noqa

    tile = Tile()
    line = Layer(tile, b"linestring")
    feature = Linestring(line)
    feature.set_id(1)
    feature.add_linestring(3)
    feature.set_point(0, 0)
    feature.set_point(10, 10)
    feature.set_point(20, 20)
    feature.commit()
    assert (
        tile.serialize()
        == b'\x1a!x\x02\n\nlinestring(\x80 \x12\x0e\x18\x02\x08\x01"\x08\t\x00\x00\x12\x14\x14\x14\x14'
    )  # noqa
