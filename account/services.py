from .models import Account
from .serializers import AccountSerializer
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from utils.lib import make_id
from utils.constants import length_id

class AccountService:
    def __init__(self) -> None:
        self.model = Account
        self.serializer = AccountSerializer

    def add(self, account: Account) -> Account:
        try:
            account.id = make_id(length_id)
            account.password = make_password(account.password)

            account.modified_at = timezone.now()
            
            account_serializer = self.serializer(data=account.__dict__)

            if account_serializer.is_valid():
                account_serializer.save()
                return account
            return None
        except Exception as e:
            print(str(e))
            return None
    
    """ def edit(self, account: Account, edited_account: Account) -> Account:
        try:

        except Exception as e:
            return None """
    def get_by_user(self, user_id: str) -> Account:
        try:
            account: Account = self.model.objects.get(user_id=user_id)
            return account
        except Exception as e:
            print(e)
            return None
        
    def get_by_id(self, id: str) -> Account:
        try:
            account: Account = self.model.objects.get(id=id)
            return account
        except Exception as e:
            return None
        
    def check_password(self, account: Account, password: str) -> bool:
        try:
            return check_password(password=password, encoded=account.password)
        except Exception as e:
            print(e)
            return False