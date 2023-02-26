from utils.dtos import Response

class RegisterResponse(Response):
    def __init__(self, success: bool, message: str) -> None:
        super().__init__(success, message)

class EditRequest:
    def __init__(self, first_name: str, last_name: str, b_date: str, phone: str, email: str, gender: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.b_date = b_date
        self.phone = phone
        self.email = email
        self.gender = gender
        