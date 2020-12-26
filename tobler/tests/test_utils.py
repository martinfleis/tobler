"""test utility functions."""

import geopandas
from libpysal.examples import load_example
from tobler.util import h3fy


def test_h3fy():
    sac1 = load_example("Sacramento1")
    sac1 = geopandas.read_file(sac1.get_path("sacramentot2.shp"))
    sac_hex = h3fy(sac1, return_geoms=True)
    assert sac_hex.shape == (364, 1)

def test_h3fy_nogeoms():
    sac1 = load_example("Sacramento1")
    sac1 = geopandas.read_file(sac1.get_path("sacramentot2.shp"))
    sac_hex = h3fy(sac1, return_geoms=False)
    assert len(sac_hex) == 364

def test_h3fy_diff_crs():
    sac1 = load_example("Sacramento1")
    sac1 = geopandas.read_file(sac1.get_path("sacramentot2.shp"))
    sac1 = sac1.to_crs(32710)
    sac_hex = h3fy(sac1, return_geoms=False)
    assert len(sac_hex) == 364
    assert sac_hex.crs.to_string() == 'EPSG:32710'
