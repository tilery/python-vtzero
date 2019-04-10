from vtzero.tile import Tile, Layer, Point, Polygon


def test_point_encoding():
    tile = Tile()
    points = Layer(tile, b'points')
    feature = Point(points)
    feature.add_points(1)
    feature.set_point(10, 10)
    feature.add_property(b'foo', b'bar')
    feature.add_property(b'x', b'y')
    feature.commit()
    assert tile.serialize() == b'\x1a0x\x02\n\x06points(\x80 \x12\r\x18\x01"\x03\t\x14\x14\x12\x04\x00\x00\x01\x01\x1a\x03foo\x1a\x01x"\x05\n\x03bar"\x03\n\x01y'  # noqa

    tile = Tile()
    points = Layer(tile, b'points')
    feature = Point(points)
    feature.set_id(1)
    feature.add_points(1)
    feature.set_point(10, 10)
    feature.add_property(b'foo', b'bar')
    feature.add_property(b'x', b'y')
    feature.commit()
    assert tile.serialize() == b'\x1a2x\x02\n\x06points(\x80 \x12\x0f\x18\x01\x08\x01"\x03\t\x14\x14\x12\x04\x00\x00\x01\x01\x1a\x03foo\x1a\x01x"\x05\n\x03bar"\x03\n\x01y'  # noqa


def test_polygon_encoding():
    tile = Tile()
    poly = Layer(tile, b'polygon')
    feature = Polygon(poly)
    feature.add_ring(5)
    feature.set_point(0, 0)
    feature.set_point(10, 0)
    feature.set_point(10, 10)
    feature.set_point(0, 10)
    feature.close_ring()
    feature.add_property(b'foo', b'bar')
    feature.add_property(b'x', b'y')
    feature.commit()
    assert tile.serialize() == b'\x1a9x\x02\n\x07polygon(\x80 \x12\x15\x18\x03"\x0b\t\x00\x00\x1a\x14\x00\x00\x14\x13\x00\x0f\x12\x04\x00\x00\x01\x01\x1a\x03foo\x1a\x01x"\x05\n\x03bar"\x03\n\x01y'  # noqa

    tile = Tile()
    poly = Layer(tile, b'polygon')
    feature = Polygon(poly)
    feature.set_id(1)
    feature.add_ring(5)
    feature.set_point(0, 0)
    feature.set_point(10, 0)
    feature.set_point(10, 10)
    feature.set_point(0, 10)
    feature.close_ring()
    feature.add_property(b'foo', b'bar')
    feature.add_property(b'x', b'y')
    feature.commit()
    assert tile.serialize() == b'\x1a;x\x02\n\x07polygon(\x80 \x12\x17\x18\x03\x08\x01"\x0b\t\x00\x00\x1a\x14\x00\x00\x14\x13\x00\x0f\x12\x04\x00\x00\x01\x01\x1a\x03foo\x1a\x01x"\x05\n\x03bar"\x03\n\x01y'  # noqa

    tile = Tile()
    poly = Layer(tile, b'polygon')
    feature = Polygon(poly)
    feature.add_ring(5)
    feature.set_point(0, 0)
    feature.set_point(10, 0)
    feature.set_point(10, 10)
    feature.set_point(0, 10)
    feature.set_point(0, 0)
    feature.add_property(b'foo', b'bar')
    feature.add_property(b'x', b'y')
    feature.commit()
    assert tile.serialize() == b'\x1a9x\x02\n\x07polygon(\x80 \x12\x15\x18\x03"\x0b\t\x00\x00\x1a\x14\x00\x00\x14\x13\x00\x0f\x12\x04\x00\x00\x01\x01\x1a\x03foo\x1a\x01x"\x05\n\x03bar"\x03\n\x01y'  # noqa
