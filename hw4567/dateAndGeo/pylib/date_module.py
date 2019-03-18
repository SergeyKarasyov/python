#!/usr/bin/python3
# 1 module: Different datatime strings (string, utf-8, base64, json) to
# python datetime object.

import base64
import unicodedata
from datetime import datetime

from pylib.own_logger import logger


def str2datetime(str):
    '''
    A function to convert string to datatime object.
    Returns - datatime object if datetime lib can parse the string
            - None if datetime lib cannot parse the string
    '''
    try:
        return datetime.strptime(str, '%b %d %Y %I:%M%p')
    except Exception:
        return None


def utf82datetime(str):
    '''
    A function to convert utf8 string to datatime object.
    Returns - datatime object if datetime lib can parse the string
            - None if datetime lib cannot parse the string
    '''
    unicodedata.normalize('NFKD', str).encode('ascii', 'ignore')
    return str2datetime(str)


def base642datetime(str):
    '''
    A function to convert base64 string to datatime object.
    Returns - datatime object if datetime lib can parse the string
            - None if datetime lib cannot parse the string
    '''
    logger.info(type(str))
    data = base64.b64decode(str)
    stringfrombase64 = "".join(chr(x) for x in data)
    logger.info(type(data))
    return str2datetime(stringfrombase64)


def main():
    date = str2datetime('Jun 1 2005  1:33PM')
    date1 = utf82datetime(u'Jun 1 2006  1:59PM')
    encoded64date = base64.b64encode(('Jun 1 2007  1:59PM').encode())
    date2 = base642datetime(encoded64date)
    logger.info(date)
    logger.info(date1)
    logger.info(date2)


if __name__ == "__main__":
    main()
