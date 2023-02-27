from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from utils.dtos import APIResponse
from .models import Account
from .dtos import LoginRequest
from utils.enums import StatusCode, RequestMethod, HeaderOption

from utils.middle_ware import JwtFilter
from utils.lib import from_dict, map,get_data
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
    if request.method == RequestMethod.POST_METHOD.value:
        data: LoginRequest = from_dict(LoginRequest, request.data)
        user: User = user_service.get_by_email(data.email)

        if user is None:
            return JsonResponse(APIResponse(message='Not found User').to_json(), status=StatusCode.BAD_REQUEST)
        
        account = account_service.get_by_user(user.id)

        if account is None:
            return JsonResponse(APIResponse(message='Not found User').to_json(), status=StatusCode.BAD_REQUEST)
        
        if account_service.check_password(account, data.password) == False:
            return JsonResponse(APIResponse(message='Not Matching Password').to_json(), status=StatusCode.BAD_REQUEST)
        token = filter.generate_access_token(account_id=account.id)
        return JsonResponse(APIResponse(success=True,message='Login Successfully', object='access_token', data=token).to_json(), status=StatusCode.OK)
    elif request.method == RequestMethod.PUT_METHOD.value:
        account_id: str = filter.get_account_id(request.headers.get(HeaderOption.AUTHORIZATION.value))

        if account_id is None:
            return JsonResponse(APIResponse(message='Invalid Token'), status=StatusCode.BAD_REQUEST)
        
        account: Account = account_service.get_by_id(account_id)
        if account is None:
            return JsonResponse(APIResponse(message='Not found Account'), status=StatusCode.NOT_FOUND)

        edit_data: Account = map(from_obj=account, Model=Account)
        edit_data = get_data(obj=edit_data, dictionary=request.data)

        if account_service.check_password(account, password=edit_data.password) == False:
            return JsonResponse(APIResponse(message='Incorrect password'), status=StatusCode.BAD_REQUEST)
        
        edited_user: User = account_service.edit(account, edit_data)
        if edited_user is None:
            return JsonResponse(APIResponse(message='Internel Error Server'), status=StatusCode.ERROR_SERVER)
        
        return JsonResponse(APIResponse(success=True, message='Change password successfully'), status=StatusCode.OK)

    


