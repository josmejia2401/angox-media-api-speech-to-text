import logging
import logging.config
import os
from pathlib import Path
from src.core_lib.utils.file import UtilidadFile

class Logger(object):

    @staticmethod
    def getLogger(dir_file=None, name='simpleExample') -> any:
        pathx = None
        logger = None
        for i in range(5):
            try:
                if i > 0 and pathx:
                    directory = os.path.dirname(pathx)
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                if dir_file is None:
                    dir_file = UtilidadFile.getPathFromResources('logging.conf')
                logging.config.fileConfig(dir_file, disable_existing_loggers=False)
                logging.getLogger('requests').setLevel(logging.ERROR)
                logging.getLogger('urllib3').setLevel(logging.ERROR)
                logging.getLogger('werkzeug').setLevel(logging.ERROR)
                logging.getLogger('requests.packages.urllib3').setLevel(logging.ERROR) 
                logging.getLogger('org.mongodb.driver').setLevel(logging.ERROR) 
                logging.getLogger('pymongo').setLevel(logging.ERROR)
                logger = logging.getLogger(name)
                break
            except Exception as e:
                if 'No such file or directory: ' in str(e):
                    pathx = str(e).split('No such file or directory: ')[1]
                    pathx = pathx[1:]
                    pathx = pathx[:-1]
                    continue
                else:
                    raise e
        if logger is None:
            raise Exception('Se requiere el logger')
        return logger