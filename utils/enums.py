from enum import IntEnum, Enum

class StatusCode(IntEnum):
    SUCCESS: int = 200
    FORBIDDEN: int = 403
    BAD_REQUEST: int = 400
    OK: int = 202
    NOT_FOUND: int = 404
    ERROR_SERVER: int = 500

class RequestMethod(Enum):
    def __str__(self):
        return str(self.value)
    POST_METHOD = 'POST'
    GET_METHOD = 'GET'
    PUT_METHOD = 'PUT'
    DELETE_METHOD = 'DELETE'


class HeaderOption(Enum):
    def __str__(self):
        return self.value
    
    CONTENT_TYPE = 'CONTENT-TYPE'
    AUTHORIZATION = 'AUTHORIZATION'

class Role(Enum):
    def __str__(self):
        return self.value
    ADMIN = 'ADMIN'
    USER = 'USER'