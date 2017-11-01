from vtzero.tile import Tile, Layer, Point


def test_point_encoding():
    tile = Tile()
    points = Layer(tile, b'points')
    feature = Point(points, 1)
    feature.add_points(1)
    feature.set_point(10, 10)
    feature.add_property(b'foo', b'bar')
    feature.add_property(b'x', b'y')
    feature.commit()
    assert tile.serialize() == b'\x1a0x\x02\n\x06points(\x80 \x12\r\x18\x01"\x03\t\x14\x14\x12\x04\x00\x00\x01\x01\x1a\x03foo\x1a\x01x"\x05\n\x03bar"\x03\n\x01y'  # noqa
