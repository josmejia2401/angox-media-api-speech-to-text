import logging
import jsonpickle
from src.core_lib.service import ServiceExternal
logger = logging.getLogger()
logger.setLevel(logging.INFO)

class Logger2(object):
    Service_External = ServiceExternal(None)
    URL = 'prod/api/v1/logs'
    
    @staticmethod
    def setLog(group, application, level, trace) -> any:
        try:
            payload = {
                "group": group,
                "application": application,
                "level": level,
                "trace": trace
            }
            Logger2.Service_External.post(url=Logger2.URL, params=None, payload=payload)
        except Exception as e:
            logger.error(e)
