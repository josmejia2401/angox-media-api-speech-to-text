import abc
from pymongo import MongoClient
from pymongo.errors import AutoReconnect
from src.core_lib.db.retry import retry
from src.core_lib.config.config_dto import ConfigDTO
from src.core_lib.utils.env import DB_MONGO_URI

retry_auto_reconnect = retry(3, (AutoReconnect,))

class Database(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def connect(self):
        pass

    @abc.abstractmethod
    def disconnect(self):
        pass

    @abc.abstractmethod
    def reconnect(self):
        pass

    @abc.abstractmethod
    def getDb(self, name):
        pass

# @Database.register
# https://api.mongodb.com/python/3.3.0/api/pymongo/mongo_client.html


class MongoDatabase(Database):
    def __init__(self, config: ConfigDTO = {}):
        super().__init__()
        self.__config = config
        self.__client = None

    def connect(self):
        try:
            if DB_MONGO_URI:
                current_uri = DB_MONGO_URI
            else:
                current_uri = self.__config.db.uri
            self.__client = MongoClient(host=current_uri,
                                        appname=self.__config.application.name,
                                        # el número máximo permitido de conexiones simultáneas a cada servidor conectado. Las solicitudes a un servidor se bloquearán si hay conexiones pendientes de maxPoolSize al servidor solicitado. El valor predeterminado es 100. No puede ser 0.
                                        maxPoolSize=self.__config.db.maxPoolSize,
                                        # el número mínimo requerido de conexiones simultáneas que el grupo mantendrá en cada servidor conectado. El valor predeterminado es 0.
                                        minPoolSize=self.__config.db.minPoolSize,
                                        # a cantidad máxima de milisegundos que una conexión puede permanecer inactiva en el grupo antes de ser eliminada y reemplazada. El valor predeterminado es Ninguno (sin límite).
                                        maxIdleTimeMS=self.__config.db.maxIdleTimeMS,
                                        # Controla cuánto tiempo (en milisegundos) el controlador esperará una respuesta después de enviar una operación de base de datos normal (sin supervisión) antes de concluir que se ha producido un error de red. El valor predeterminado es Ninguno (sin tiempo de espera).
                                        socketTimeoutMS=self.__config.db.socketTimeoutMS,
                                        # Controla cuánto tiempo (en milisegundos) esperará el controlador durante la supervisión del servidor cuando se conecta un nuevo socket a un servidor antes de concluir que el servidor no está disponible. El valor predeterminado es 20000 (20 segundos).
                                        connectTimeoutMS=self.__config.db.connectTimeoutMS,
                                        # Controla cuánto tiempo (en milisegundos) esperará el controlador para encontrar un servidor apropiado disponible para llevar a cabo una operación de base de datos; mientras está esperando, se pueden realizar múltiples operaciones de monitoreo del servidor, cada una controlada por connectTimeoutMS . El valor predeterminado es 30000 (30 segundos).
                                        serverSelectionTimeoutMS=self.__config.db.serverSelectionTimeoutMS
                                        )
            #serverStatusResult = self.__client.angos.command("serverStatus")
            #print(serverStatusResult)
            #for name in self.__client.list_database_names():  
            #    print(name)  
        except Exception as e:
            raise e

    def disconnect(self):
        if self.__client:
            self.__client.close()

    @retry_auto_reconnect
    def reconnect(self):
        self.connect()

    def getDb(self, name: str = None):
        if name and self.__client:
            return self.__client[name]
        elif self.__client:
            return self.__client[self.__config.db.dbName]
        else:
            raise Exception('No se encuentra el cliente DB')
