#!/usr/bin/python3
import json
import os
from pathlib import Path
from src.core_lib.config.config_dto import ConfigDTO
from src.core_lib.utils.file import UtilidadFile

class Config(object):

    def __init__(self, dir_file=None):
        self.__dir_file = dir_file
        self.__configJson = None
        self.__loadJson()

    def __loadJson(self):
        if self.__dir_file:
            config_json = UtilidadFile.loadFileFromResourcesAsJson('config.json', self.__dir_file)
        else:
            config_json = UtilidadFile.loadFileFromResourcesAsJson('config.json')
        self.__configJson = ConfigDTO(config_json)

    def getConfig(self) -> ConfigDTO:
        return self.__configJson
