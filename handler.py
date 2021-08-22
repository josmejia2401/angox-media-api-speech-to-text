#!/usr/bin/python3
from src.main.controllers.controller import Controller1
from src.main.utils.core import config
from src.core_lib.logger2 import Logger2
import jsonpickle

controller = Controller1(config)

def lambda_handler(event, context):
    try:
        controller.speechToText({"voice": None })
        #Logger2.setLog('media', config.application.name, 'INFO', jsonpickle.encode(event))
        return "ok"
    except Exception as e:
        print(e)
        #Logger2.setLog('media', config.application.name, 'ERROR', str(e))
        raise e

if __name__ == '__main__':
    try:
       lambda_handler({"name": "jose"}, None)
    except Exception as e:
        Logger2.setLog('media', config.application.name, 'ERROR', str(e))