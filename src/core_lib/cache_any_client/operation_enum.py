from enum import Enum, unique

@unique
class OperationEnum(Enum):
    GET = 1
    ADD = 2
    PUT = 3
    POP = 4
    REMOVE = 5