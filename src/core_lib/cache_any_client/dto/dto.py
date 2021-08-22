from src.core_lib.cache_any_client.operation_enum import OperationEnum

class Statement:
    def __init__(self, jsonAsString=None):
        self.id: str = None
        self.value: any = None
        if jsonAsString is None:
            return
        if 'id' in jsonAsString and jsonAsString['id'] is not None:
            self.id = jsonAsString['id']
        if 'value' in jsonAsString and jsonAsString['value'] is not None:
            self.value = jsonAsString['value']

class Operation:
    def __init__(self, jsonAsString=None):
        self.operation: OperationEnum = None
        self.statement:Statement = None
        if jsonAsString is None:
            return
        if 'operation' in jsonAsString and jsonAsString['operation'] is not None:
            self.operation = OperationEnum(jsonAsString['operation'])
        if 'statement' in jsonAsString and jsonAsString['statement'] is not None:
            self.statement = Statement(jsonAsString['statement'])
        
            