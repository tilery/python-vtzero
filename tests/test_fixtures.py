"""fixtures."""

import json
from pathlib import Path

import pytest

from vtzero.tile import VectorTile

ROOT = Path(__file__).parent.parent / "vendor/mvt-fixtures/fixtures"

# Magic: Generate tests from yml.
# def pytest_generate_tests(metafunc):
#     if {'info', 'data', 'mvt'} <= set(metafunc.fixturenames):
#         root = Path(__file__).parent.parent / 'vendor/mvt-fixtures/fixtures'
#         # print([x for x in fixtures.iterdir() if x.is_dir()])
#         fixtures = []
#         paths = list(root.iterdir())
#         paths.sort()
#         for path in paths:
#             fixtures.append([
#                 json.loads((path / 'info.json').open('r').read()),
#                 json.loads((path / 'tile.json').open('r').read()),
#                 (path / 'tile.mvt').open('rb').read(),
#             ])
#         metafunc.parametrize("info,data,mvt", fixtures)


@pytest.fixture
def fixture():
    """data fixtures."""

    def _(id):
        path = ROOT / id
        with (path / "info.json").open("r") as f:
            info = json.loads(f.read())
        with (path / "tile.json").open("r") as f:
            data = json.loads(f.read())
        with (path / "tile.mvt").open("rb") as f:
            mvt = f.read()
        return info, data, mvt

    return _


def first_feature(tile):
    """check and return feature."""
    assert not tile.empty()
    assert len(tile) == 1
    layer = next(tile)
    assert layer.name == b"hello"
    assert layer.version == 2
    assert layer.extent == 4096
    assert len(layer) == 1
    return next(layer)


def test_empty_tile(fixture):
    """empty tile fixture."""
    info, data, mvt = fixture("001")
    tile = VectorTile(mvt)
    assert tile.empty()
    assert len(tile) == 0


def test_single_point_without_id(fixture):
    """Point."""
    info, data, mvt = fixture("002")
    tile = VectorTile(mvt)
    feature = first_feature(tile)
    assert not feature.has_id()
    assert feature.id == 0
    assert feature.geometry_type == VectorTile.POINT
    # assert feature.geometry == [25, 17]
