import pytest
from geopy import Point

from pylib.geo_module import string2geo


def test_string2geo():
    geoString = '41.5,-81.0'
    geoToCompare = Point(geoString)
    assert geoToCompare == string2geo(geoString)
