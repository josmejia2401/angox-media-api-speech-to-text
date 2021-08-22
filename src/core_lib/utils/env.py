#!/usr/bin/python3
import os
CURRENT_ENVIRONMENT = 'DEV'
DB_MONGO_URI = None
URL_LOGGER2 = None
if 'DB_MONGO_URI' in os.environ:
    DB_MONGO_URI = os.environ['DB_MONGO_URI']
if 'URL_LOGGER2' in os.environ:
    URL_LOGGER2 = os.environ['URL_LOGGER2']