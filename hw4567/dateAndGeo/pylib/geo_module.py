#!/usr/bin/python3
# 2 module: convert strings to correct GEO coordinates (lat/lon). Examples:
# 41 25 01N and 120 58 57W 41°25'01"N and 120°58'57"W
# S17 33 08.352 and W69 01 29.74 to 41.250000, -120.976200
from geopy.point import Point
from pylib.own_logger import logger


def string2geo(geo_coordinates):
    '''
    A function to convert string to geopy object.
    Returns - geopy object if geopy lib can parse the string
            - None if geopy lib cannot parse the string
    '''
    try:
        return Point(geo_coordinates)
    except Exception:
        return None


def main():
    logger.info(string2geo('41.5,-81.0'))
    logger.info(string2geo('41.5 N -81.0 W'))
    logger.info(string2geo('''3 26' 22" N 23 27' 30" E'''))


if __name__ == "__main__":
    main()
