from src.core_lib.config.config_dto import ConfigDTO
from src.core_lib.service import ServiceDataBase
 
class ControllerDataBase(object):

    def __init__(self, config:ConfigDTO = None, collection_name = None):
        self.__config = config
        self.__service = ServiceDataBase(config=config, collection_name=collection_name)
    
    def get_config(self) -> ConfigDTO:
        return self.__config

    def get_service(self) -> ServiceDataBase:
        return self.__service

class Controller(object):

    def __init__(self, config:ConfigDTO = None):
        self.__config = config
    
    def get_config(self) -> ConfigDTO:
        return self.__config
