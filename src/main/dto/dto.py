from src.main.utils.core import DTO
import datetime

class SpeechDTO(DTO): 
    def __init__(self, dataAsJson={}, ignored_none=False, update=False):
        DTO.__init__(self, dataAsJson, ignored_none)
        self.data = None
        if dataAsJson is None:
            return
        if 'data' in dataAsJson and dataAsJson['data']:
            self.data = dataAsJson['data']