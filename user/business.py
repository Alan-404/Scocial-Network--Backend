from .services import UserService
from .models import User

# Account
from account.models import Account
from account.services import AccountService

# Utils
from utils.lib import from_dict


class UserBusiness:
    def __init__(self) -> None:
        self.service = UserService()
        self.account_service = AccountService()

    def register_user(self, data: dict) -> User:
        user: User = from_dict(Model=User, dictionary=data)
        account: Account = from_dict(Model=Account, dictionary=data)
        
        saved_user: User = self.service.add(user)
    
        if saved_user is not None:
            account.user_id = saved_user.id
            saved_account: Account = self.account_service.add(account)
            if saved_account is not None:
                return saved_user
        return None
    
    def get_by_account_id(self, id: str) -> User:
        account: Account = self.account_service.get_by_id(id)

        if account is None:
            return None
        
        user: User = self.service.get_by_id(account.user_id)

        if user is None:
            return None
        
        return user

        