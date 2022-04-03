from configparser import ConfigParser
import os


class ConfigReader:
    __cwd = os.getcwd()
    __root_path = os.path.dirname(__cwd)
    __config_path = __root_path + "/config.ini"

    def read_config(self, config):
        configurations = ConfigParser()
        configurations.read(self.__config_path)
        return configurations["appconfigs"][config]
