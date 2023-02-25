from .services import AccountService
from utils.lib import from_dict
from .dtos import LoginRequest

from .models import Account

from user.models import User
from user.services import UserService

class AccountBusiness:
    def __init__(self) -> None:
        self.service = AccountService()
        self.user_service = UserService()

    def login(self, info: dict) -> Account:
        data: LoginRequest = from_dict(LoginRequest, info)
        user: User = self.user_service.get_by_email(data.email)

        if user is None:
            return None
        
        account: Account = self.service.get_by_user(user.id)

        if account is None:
            return None
        
        if self.service.check_password(account, data.password):
            return account
        