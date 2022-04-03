import json
import os

from src.utils.config_reader import ConfigReader


class JsonReader:
    __cr = ConfigReader()
    __cwd = os.getcwd()
    __file_path = os.path.dirname(__cwd) + "/" + __cr.read_config("test.data.dir")

    def read_json(self, file_name, key, value):
        if "json" in file_name:
            self.__file_path += "/" + file_name
        else:
            self.__file_path += "/" + file_name + ".json"

        with open(self.__file_path) as data_file:
            data = json.load(data_file)
            for item in data:
                if item[key] == value:
                    return item
