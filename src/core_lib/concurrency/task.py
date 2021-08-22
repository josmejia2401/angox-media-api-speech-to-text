#!/usr/bin/python3
import socket
import time
import sys
from abc import ABCMeta, abstractmethod
from urllib.parse import urlparse, ParseResult

class ITask(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @classmethod
    def version(self):
        return "1.0"

    @abstractmethod
    def run(self):
        raise NotImplementedError
