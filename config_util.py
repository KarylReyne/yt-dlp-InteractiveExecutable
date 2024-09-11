import json
import os

default_path = "./config"
masterconfigfile = "config.json"


def write_config(config, path=default_path, file=masterconfigfile):
    with open(path+os.sep+file, 'w') as configfile:
        json.dump(config, configfile, indent=4)
        configfile.close()


def edit_config(config_dict, path=default_path, file=masterconfigfile):
    with open(path+os.sep+file, 'r') as configfile:
        config = json.load(configfile)
        for key in config_dict:
            config[key] = config_dict[key]
        configfile.close()
    write_config(config, default_path, masterconfigfile)


def get_config(key, path=default_path, file=masterconfigfile):
    with open(path+os.sep+file, 'r') as configfile:
        config = json.load(configfile)
        value = config[key]
    return value


class InvalidConfig(Exception):
    """The config file contains invalid parameters"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)