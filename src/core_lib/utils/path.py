#!/usr/bin/python3
from urllib.parse import urlparse
import random
from src.core_lib.config.config_dto import ConfigDTO

class UtilidadPath(object):

    def __init__(self, config: ConfigDTO = None):
        self.config = config

    def allows_path(self, original_path = None) -> str:
        if not original_path:
            return None, True
        if original_path[0] != '/':
            original_path = '/' + original_path
        if len(self.config.routes.routes) > 0:
            for route in self.config.routes.routes:
                if not route.url or len(route.url) == 0:
                    continue
                num_asterisks = str(route.path).count('*')
                route_url = None
                route_path = route.path
                if len(route.url) > 0:
                    route_url = random.choice(route.url)
                if num_asterisks == 0:
                    if original_path == route_path:
                        return f'{route_url}{original_path}', route.need_authentication
                elif num_asterisks == 1:
                    new_path = route_path.replace('*', '')
                    new_path = original_path.replace(new_path, '')
                    num_asterisks_ = new_path.count('/')
                    if num_asterisks_ < 2:
                        return f'{route_url}{original_path}', route.need_authentication
                else:
                    new_path = route_path.replace('*', '')
                    new_path = new_path.replace('//', '/')
                    if new_path in original_path:
                        return f'{route_url}{original_path}', route.need_authentication
            raise Exception('La ruta no coincide (3)', original_path)
        else:
            raise Exception('No hay routes definidos')