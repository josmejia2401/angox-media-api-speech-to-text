import socket
import pickle
import time
import sys
from src.core_lib.cache_any_client.dto.dto import Operation, Statement
from  src.core_lib.cache_any_client.operation_enum import OperationEnum

class CacheAny:

    def __init__(self, hostname='localhost', port=65035):
        self.__hostname = hostname
        self.__port = port

    def __get_connection(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((self.__hostname, self.__port))
            return s
        except Exception as e:
            raise e
    
    def __close(self, s):
        if s:
            try: 
                s.shutdown(socket.SHUT_RDWR)
            except: 
                pass
            try: 
                s.close()
            except: 
                pass

    def __send(self, conn, data):
        try:
            data = pickle.dumps(data)
            conn.sendall(data)
        except Exception as e:
            raise e
    
    def __recv(self, conn):
        try:
            data = b''
            deadline = time.time() + 10
            while True:
                if time.time() >= deadline:
                    raise Exception('READ_TIMEOUT CUSTOM')
                conn.settimeout(deadline - time.time())
                chunk = conn.recv(1024, socket.MSG_WAITALL)
                length_1 = sys.getsizeof(chunk)
                if length_1 > 0:
                    data += chunk
                else:
                    break
                if length_1 < 1024:
                    break
                if length_1 < 1_057:
                    break
                time.sleep(0.05)
            return data
        except Exception as e:
            raise e
    
    def get(self, k):
        conn = None
        try:
            operation: Operation = Operation()
            operation.statement = Statement()
            operation.statement.id = k
            operation.statement.value = None
            operation.operation = OperationEnum.GET
            conn = self.__get_connection()
            self.__send(conn, operation)
            data = self.__recv(conn)
            if data:
                if isinstance(data, Exception):
                    raise Exception(data)
                data = pickle.loads(data)
            return data
        except Exception as e:
            raise e
        finally:
            self.__close(conn)

    def add(self, k, v):
        conn = None
        try:
            operation: Operation = Operation()
            operation.statement = Statement()
            operation.statement.id = k
            operation.statement.value = v
            operation.operation = OperationEnum.ADD
            conn = self.__get_connection()
            self.__send(conn, operation)
            data = self.__recv(conn)
            if data:
                data = pickle.loads(data)
                if isinstance(data, Exception):
                    raise Exception(data)
            return data
        except Exception as e:
            raise e
        finally:
            self.__close(conn)

    def put(self, k, v):
        conn = None
        try:
            operation: Operation = Operation()
            operation.statement = Statement()
            operation.statement.id = k
            operation.statement.value = v
            operation.operation = OperationEnum.PUT
            conn = self.__get_connection()
            self.__send(conn, operation)
            data = self.__recv(conn)
            if data:
                if isinstance(data, Exception):
                    raise Exception(data)
                data = pickle.loads(data)
            return data
        except Exception as e:
            raise e
        finally:
            self.__close(conn)

    def pop(self, k):
        conn = None
        try:
            operation: Operation = Operation()
            operation.statement = Statement()
            operation.statement.id = k
            operation.statement.value = None
            operation.operation = OperationEnum.POP
            conn = self.__get_connection()
            self.__send(conn, operation)
            data = self.__recv(conn)
            if data:
                if isinstance(data, Exception):
                    raise Exception(data)
                data = pickle.loads(data)
            return data
        except Exception as e:
            raise e
        finally:
            self.__close(conn)

    def remove(self, k):
        conn = None
        try:
            operation: Operation = Operation()
            operation.statement = Statement()
            operation.statement.id = k
            operation.statement.value = None
            operation.operation = OperationEnum.REMOVE
            conn = self.__get_connection()
            self.__send(conn, operation)
            data = self.__recv(conn)
            if data:
                if isinstance(data, Exception):
                    raise Exception(data)
                data = pickle.loads(data)
            return data
        except Exception as e:
            raise e
        finally:
            self.__close(conn)