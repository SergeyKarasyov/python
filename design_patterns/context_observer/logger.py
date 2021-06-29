#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""[summary]
"""
import logging
import logging.config
import os


def get_logger(name):
    """[summary]

    Arguments:
        name {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    logfile = os.environ.get('LOGFILE', '/tmp/{}.log'.format(name))
    result_logger = logging.getLogger(name)
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(logfile, encoding='utf8')
    formatter = logging.Formatter('[%(asctime)s]'
                                  '[%(processName)s %(process)-6d]'
                                  '[%(filename)s %(lineno)d]'
                                  '[%(funcName)s]'
                                  '[%(levelname)s]'
                                  '%(message)s')
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    result_logger.addHandler(stream_handler)
    result_logger.addHandler(file_handler)
    result_logger.setLevel(logging.DEBUG)
    return result_logger


LOGGER = get_logger('ssh_handler')
