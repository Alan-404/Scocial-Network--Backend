from utils.dtos import Response

class RegisterResponse(Response):
    def __init__(self, success: bool, message: str) -> None:
        super().__init__(success, message)
        