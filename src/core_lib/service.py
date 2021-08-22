import requests
from requests.exceptions import HTTPError
from pymongo import DESCENDING, ASCENDING
from bson import ObjectId
from src.core_lib.config.config_dto import ConfigDTO
from src.core_lib.db.db import MongoDatabase

class ServiceDataBase(object):

    def __init__(self, config:ConfigDTO = None, collection_name = None):
        self.__db_client = MongoDatabase(config)
        self.__db_client.connect()
        self.__db = self.__db_client.getDb()
        self.__collection = self.__db[collection_name]
    
    def create(self, payload=None) -> any:
        document = self.__collection.insert_one(payload)
        if document:
            oid = str(document.inserted_id)
            document = self.__collection.find_one({ "_id": ObjectId(oid) })
            if document:
                document['id'] = str(document['_id'])
                del document['_id']
                return document
        return None

    def update(self, id=None, payload=None, upsert=False) -> any:
        response = self.__collection.update_one({ "_id": ObjectId(id) }, { "$set": payload }, upsert=upsert)
        if response and response.modified_count > 0:
            document = self.__collection.find_one({ "_id": ObjectId(id) })
            if document:
                document['id'] = str(document['_id'])
                del document['_id']
                return document
        return None
    
    def delete(self, id=None) -> int:
        response = self.__collection.delete_one({ "_id": ObjectId(id) })
        return response.deleted_count

    def get(self, id=None) -> any:
        document = self.__collection.find_one({ "_id": ObjectId(id) })
        if document:
            document['id'] = str(document['_id'])
            del document['_id']
            return document
        return None

    def get_one(self, payload_where=None) -> any:
        document = self.__collection.find_one(payload_where)
        if document:
            document['id'] = str(document['_id'])
            del document['_id']
            return document
        return None

    def get_many(self, payload_where=None, order_by=None, offset=None, limit=None) -> any:
        documents = None
        if order_by is None:
            order_by = [("_id", DESCENDING)]
        if offset and limit:
            count = self.get_count()
            if (offset * limit) > count:
                limit = (offset * limit) - count
            #.sort([("field1", pymongo.ASCENDING), ("field2", pymongo.DESCENDING)]))
            documents = list(self.__collection.find(payload_where).sort(order_by).skip(offset).limit(limit))
        else:
            documents = list(self.__collection.find(payload_where).sort(order_by))
        if documents and len(documents) > 0:
            for document in documents:
                document['id'] = str(document['_id'])
                del document['_id']
        return documents
    
    def get_count(self) -> any:
        return self.__collection.count()

class ServiceExternal(object):

    def __init__(self, config:ConfigDTO = None):
        self.__config = config
    
    def get(self, url, params=None, is_json=True):
        try:
            response = requests.get(url, params=params)
            if response and response.status_code > 299:
                raise Exception(response.content)
            if is_json == True:
                return response.json()
            return response.content
        except HTTPError as e:
            raise e
        except Exception as e:
            raise e
    
    def post(self, url, params=None, payload=None, data=None, is_json=True):
        try:
            response = requests.post(url, data=data, json=payload, params=params)
            if response and response.status_code > 299:
                raise Exception(response.content)
            if is_json == True:
                return response.json()
            return response.content
        except HTTPError as e:
            raise e
        except Exception as e:
            raise e
    def put(self, url, params=None, payload=None, data=None, is_json=True):
        try:
            response = requests.put(url, data=data, json=payload, params=params)
            if response and response.status_code > 299:
                raise Exception(response.content)
            if is_json == True:
                return response.json()
            return response.content
        except HTTPError as e:
            raise e
        except Exception as e:
            raise e

    def delete(self, url, params=None, payload=None, data=None, is_json=True):
        try:
            response = requests.delete(url, data=data, json=payload, params=params)
            if response and response.status_code > 299:
                raise Exception(response.content)
            if is_json == True:
                return response.json()
            return response.content
        except HTTPError as e:
            raise e
        except Exception as e:
            raise e