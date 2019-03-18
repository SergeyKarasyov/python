#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Write multiprocessing module which convert all files in local directory (json, yaml) to list of 
# python objects where each file type shall be handled in separately process and each file i separately thread. Please use multiprocessing POOL

import multiprocessing
import json_reader
import yaml_reader


def parseconfig(config_name):
    if not os.path(config_name).exists():
        sys.exit("File doesn't exist: {}".format(config_name))
    

