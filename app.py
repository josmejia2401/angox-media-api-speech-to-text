#!/usr/bin/python3
from src.main.main import app
from src.main.utils.core import config, loggerx

if __name__ == '__main__':
    try:
        if config.server.debug == True:
            app.run(host=config.server.host, port=config.server.port, debug=config.server.debug)
        else:
            app.run()
    except Exception as e:
        loggerx.error(e)