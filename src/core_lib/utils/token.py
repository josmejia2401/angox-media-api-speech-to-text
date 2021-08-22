import secrets
from enum import Enum, unique

def generate_token(lenght=32):
    return secrets.token_urlsafe(lenght)

@unique
class TypeTokenEnum(Enum):
    SESSION = 1
    APPLICATION = 2