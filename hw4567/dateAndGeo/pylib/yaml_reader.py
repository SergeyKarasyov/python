#! /usr/bin/python3
# Write module which read YAML format config file and create ONE
# config<filename> class which convert each YAML item to class attribute
# magically (smile)

import os
import yaml
import pprint

config_name = "yaml_reader.yml"


class obsoleteYamlConfiguration():
    '''stupid solution'''
    classes = []

    def __init__(self, yaml_data):
        [self.classes.append({key: value}) for key, value in yaml_data.items()]

    def __repr__(self):
        return "".join(str(value.keys()) +
                       str(value.values()) +
                       "\n" for value in (self.classes))


class yamlconfiguration():
    '''ideal solution'''

    def __init__(self, kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return "".join(str(attr) + str(getattr(self, attr)) +
                       "\n" for attr in dir(self) if not attr.startswith('__'))


def read_yaml(configName):
    '''
    function to read yaml file.
    Returns - dict with the data that was read from yaml, if file exists
            - None if file doesn't exist
    '''
    if not (os.path.exists(configName)):
        print("No config was found. Recheck if it exists: {}".format(configName))
        return None

    with open(configName, 'r') as configuration:
        conf = yaml.safe_load(configuration)
    print(type(conf))
    return conf


def main():
    print("just reading/printing input data in yaml reader.")
    configurationMap = read_yaml(config_name)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(configurationMap)
    for key, value in configurationMap.items():
        print("{} {}".format(key, value))

    print("class with dict solution.")
    confi = yamlconfiguration(configurationMap)
    print(confi)

    print("class with attrs solution.")
    confi2 = obsoleteYamlConfiguration(configurationMap)
    print(confi2)


if __name__ == "__main__":
    main()
