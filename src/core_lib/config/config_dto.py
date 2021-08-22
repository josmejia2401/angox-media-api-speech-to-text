#!/usr/bin/python3

class ApplicationDTO:
    def __init__(self, jsonData={}):
        self.name = None
        if 'application' in jsonData:
            jsonServer = jsonData['application']
            if 'name' in jsonServer and jsonServer['name']:
                self.name = jsonServer['name']

class ConcurrencyDTO:
    def __init__(self, jsonData={}):
        self.pool_size = 1000
        self.pool_size_core = 1
        self.pool_size_max = 50
        if 'concurrency' in jsonData:
            jsonServer = jsonData['concurrency']
            if 'pool_size' in jsonServer and jsonServer['pool_size']:
                self.pool_size = jsonServer['pool_size']
            if 'pool_size_core' in jsonServer and jsonServer['pool_size_core']:
                self.pool_size_core = jsonServer['pool_size_core']
            if 'pool_size_max' in jsonServer and jsonServer['pool_size_max']:
                self.pool_size_max = jsonServer['pool_size_max']

class SocketDTO:
    def __init__(self, jsonData={}):
        self.max_request_len = 1024
        self.connection_timeout = 10
        self.read_timeout = 10
        self.queue_size = 200
        if 'socket' in jsonData:
            jsonServer = jsonData['socket']
            if 'max_request_len' in jsonServer and jsonServer['max_request_len'] is not None:
                self.max_request_len = jsonServer['max_request_len']
            if 'connection_timeout' in jsonServer and jsonServer['connection_timeout'] is not None:
                self.connection_timeout = jsonServer['connection_timeout']
            if 'read_timeout' in jsonServer and jsonServer['read_timeout'] is not None:
                self.read_timeout = jsonServer['read_timeout']
            if 'queue_size' in jsonServer and jsonServer['queue_size'] is not None:
                self.queue_size = jsonServer['queue_size']

class ProxyDTO:
    def __init__(self, jsonData={}):
        self.retries = 3
        self.backoff_factor = 0.3
        self.status_forcelist = [500, 502, 504]
        self.pool_connections = 10
        self.pool_maxsize = 100
        self.pool_block = True
        self.connection_timeout = 10
        self.read_timeout = 10
        if 'proxy' in jsonData:
            jsonServer = jsonData['proxy']
            if 'retries' in jsonServer and jsonServer['retries'] is not None:
                self.retries = jsonServer['retries']
            if 'backoff_factor' in jsonServer and jsonServer['backoff_factor'] is not None:
                self.backoff_factor = jsonServer['backoff_factor']
            if 'status_forcelist' in jsonServer and jsonServer['status_forcelist'] is not None:
                self.status_forcelist = jsonServer['status_forcelist']
            if 'pool_connections' in jsonServer and jsonServer['pool_connections'] is not None:
                self.pool_connections = jsonServer['pool_connections']
            if 'pool_maxsize' in jsonServer and jsonServer['pool_maxsize'] is not None:
                self.pool_maxsize = jsonServer['pool_maxsize']
            if 'pool_block' in jsonServer and jsonServer['pool_block'] is not None:
                self.pool_block = jsonServer['pool_block']
            if 'connection_timeout' in jsonServer and jsonServer['connection_timeout'] is not None:
                self.connection_timeout = jsonServer['connection_timeout']
            if 'read_timeout' in jsonServer and jsonServer['read_timeout'] is not None:
                self.read_timeout = jsonServer['read_timeout']

class ServerDTO:
    def __init__(self, jsonData={}):
        self.port = 8080
        self.host = '0.0.0.0'
        self.hostname = 'locahost'
        self.debug = True
        self.ssl = False
        if 'server' in jsonData:
            jsonServer = jsonData['server']
            if 'port' in jsonServer and jsonServer['port']:
                self.port = jsonServer['port']
            if 'host' in jsonServer and jsonServer['host']:
                self.host = jsonServer['host']
            if 'hostname' in jsonServer and jsonServer['hostname']:
                self.hostname = jsonServer['hostname']
            if 'debug' in jsonServer and jsonServer['debug'] is not None:
                self.debug = jsonServer['debug']
            if 'ssl' in jsonServer and jsonServer['ssl'] is not None:
                self.ssl = jsonServer['ssl']

class DbDTO:
    def __init__(self, jsonData={}):
        self.uri = None
        self.uri2 = None
        self.dbName = None
        self.maxPoolSize=7
        self.minPoolSize=0
        self.maxIdleTimeMS=20000
        self.socketTimeoutMS=20000
        self.connectTimeoutMS=20000
        self.serverSelectionTimeoutMS=20000
        if 'db' in jsonData:
            jsonServer = jsonData['db']
            if 'uri' in jsonServer and jsonServer['uri']:
                self.uri = jsonServer['uri']
            if 'uri2' in jsonServer and jsonServer['uri2']:
                self.uri2 = jsonServer['uri2']
            if 'dbName' in jsonServer and jsonServer['dbName']:
                self.dbName = jsonServer['dbName']
            if 'maxPoolSize' in jsonServer and jsonServer['maxPoolSize']:
                self.maxPoolSize = jsonServer['maxPoolSize']
            if 'minPoolSize' in jsonServer and jsonServer['minPoolSize']:
                self.minPoolSize = jsonServer['minPoolSize']
            if 'maxIdleTimeMS' in jsonServer and jsonServer['maxIdleTimeMS']:
                self.maxIdleTimeMS = jsonServer['maxIdleTimeMS']
            if 'socketTimeoutMS' in jsonServer and jsonServer['socketTimeoutMS']:
                self.socketTimeoutMS = jsonServer['socketTimeoutMS']
            if 'connectTimeoutMS' in jsonServer and jsonServer['connectTimeoutMS']:
                self.connectTimeoutMS = jsonServer['connectTimeoutMS']
            if 'serverSelectionTimeoutMS' in jsonServer and jsonServer['serverSelectionTimeoutMS']:
                self.serverSelectionTimeoutMS = jsonServer['serverSelectionTimeoutMS']

class RouteDTO:
    def __init__(self, jsonData={}):
        self.path = ''
        self.url = ''
        self.need_authentication = False
        self.methods = []
        if 'path' in jsonData:
            self.path = jsonData['path']
        if 'url' in jsonData:
            self.url = jsonData['url']
        if 'need_authentication' in jsonData:
            self.need_authentication = jsonData['need_authentication']
        if 'methods' in jsonData:
            self.methods = jsonData['methods']

class RoutesDTO:
    def __init__(self, jsonData={}):
        self.routes = []
        if 'routes' in jsonData:
            jsonServer = jsonData['routes']
            if jsonServer and len(jsonServer) > 0:
                for route in jsonServer:
                    self.routes.append(RouteDTO(route))
                
class ApiDTO:
    def __init__(self, jsonData={}):
        self.name = ''
        self.url = ''
        if 'name' in jsonData:
            self.name = jsonData['name']
        if 'url' in jsonData:
            self.url = jsonData['url']

class ApisDTO:
    def __init__(self, jsonData={}):
        self.apis = []
        if 'apis' in jsonData:
            jsonServer = jsonData['apis']
            if jsonServer and len(jsonServer) > 0:
                for api in jsonServer:
                    self.apis.append(ApiDTO(api))

class ConfigDTO:
    def __init__(self, jsonData={}):
        self.application = ApplicationDTO(jsonData)
        self.server = ServerDTO(jsonData)
        self.db = DbDTO(jsonData)
        self.routes = RoutesDTO(jsonData)
        self.currency = ConcurrencyDTO(jsonData)
        self.socket = SocketDTO(jsonData)
        self.proxy = ProxyDTO(jsonData)
        self.apis = ApisDTO(jsonData)
