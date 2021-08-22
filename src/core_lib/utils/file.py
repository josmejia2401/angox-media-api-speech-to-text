#!/usr/bin/python3
import json
import os
from pathlib import Path
from src.core_lib.config.config_dto import ConfigDTO


class UtilidadFile(object):

    def __init__(self):
        pass
    
    @staticmethod
    def loadFileFromResourcesAsJson(name=None, current_dir=None):
        if current_dir is None:
            current_dir = Path(__file__).parent
        file_path = os.path.join(current_dir, 'src', 'resources', name)
        contBreak = 0
        while os.path.exists(file_path) == False:
            if contBreak > 5:
                break
            current_dir = Path(current_dir).parent
            file_path = os.path.join(current_dir, 'src', 'resources', name)
            contBreak += 1
        contents = None
        with open(file_path) as dataFile:
            contents = json.load(dataFile)
        return contents

    @staticmethod
    def getPathFromResources(name=None, current_dir=None):
        if current_dir is None:
            current_dir = Path(__file__).parent
        file_path = os.path.join(current_dir, 'src', 'resources', name)
        contBreak = 0
        while os.path.exists(file_path) == False:
            if contBreak > 5:
                break
            current_dir = Path(current_dir).parent
            file_path = os.path.join(current_dir, 'src', 'resources', name)
            contBreak += 1
        return file_path
