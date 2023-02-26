from .models import User
from .serializers import UserSerializer
from utils.lib import make_id
from utils.constants import length_id
from django.utils import timezone

class UserService:
    def __init__(self) -> None:
        self.model = User
        self.serializer = UserSerializer

    def add(self, user: User) -> User:
        try:
            user.id = make_id(length=length_id)
            user.created_at = timezone.now()
            user.modified_at = timezone.now()
  
            user_serializer = self.serializer(data=user.__dict__)
            if user_serializer.is_valid():
                user_serializer.save()
                return user
            return None
        except Exception as e:
            print(e)
            return None
    
    def edit(self, user: User, edit_data: User) -> User:
        try:
            edit_data.modified_at = timezone.now()

            user_serializer: UserSerializer = self.serializer(user, data=edit_data.__dict__)
            if user_serializer.is_valid():
                user_serializer.save()

                return edit_data
            else:
                print(user_serializer.errors)
            return None
        except Exception as e:
            print(e)
            return None

    def get_by_email(self, email: str) -> User:
        try:
            user= self.model.objects.get(email=email)
            return user
        except Exception as e:
            return None

    def get_by_id(self, id: str) -> User:
        try:
            user: User = self.model.objects.get(id=id)
            return user
        except Exception as e:
            return None
        
        
