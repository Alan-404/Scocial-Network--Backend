from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from utils.dtos import APIResponse
from .models import Account
from .dtos import LoginResponse, LoginRequest
from utils.constants import StatusCode

from utils.middle_ware import JwtFilter
from utils.lib import from_dict
from .services import AccountService
from .models import Account
from user.services import UserService
from user.models import User

# Create your views here.

account_service = AccountService()
user_service = UserService()

filter = JwtFilter()

@api_view(['POST'])
def auth(request: Request) -> JsonResponse:
    if request.method == 'POST':
        data: LoginRequest = from_dict(LoginRequest, request.data)
        user: User = user_service.get_by_email(data.email)

        if user is None:
            return JsonResponse(APIResponse(message='Not found User').to_json(), status=StatusCode.BAD_REQUEST)
        
        account: Account = account_service.get_by_user(user.id)

        if account is None:
            return JsonResponse(APIResponse(message='Not found User').to_json(), status=StatusCode.BAD_REQUEST)

        if account_service.check_password(account, data.password) == False:
            return JsonResponse(APIResponse(message='Not Matching Password').to_json(), status=StatusCode.BAD_REQUEST)
        token: str = filter.generate_access_token(account_id=account.id)
        return JsonResponse(APIResponse(success=True,message='Login Successfully', object='access_token', data=token).to_json(), status=StatusCode.OK)

    


