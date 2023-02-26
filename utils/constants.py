from enum import IntEnum

length_id: int = 21


class StatusCode(IntEnum):
    SUCCESS: int = 200
    FORBIDDEN: int = 403
    BAD_REQUEST: int = 400
    OK: int = 202
    NOT_FOUND: int = 404
    ERROR_SERVER: int = 500