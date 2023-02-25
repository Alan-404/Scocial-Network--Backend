from utils.dtos import Response

class LoginResponse(Response):
    def __init__(self, success: bool, message: str, access_token: str) -> None:
        super().__init__(success, message)
        self.access_token = access_token



# Requests
class LoginRequest:
    def __init__(self, email: str = '', password: str = '') -> None:
        self.email = email
        self.password = password