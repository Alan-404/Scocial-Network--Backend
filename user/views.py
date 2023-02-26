from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from utils.constants import StatusCode
from utils.middle_ware import JwtFilter
from utils.lib import from_dict, map, get_data
from utils.dtos import APIResponse
from .models import User
from account.models import Account
from account.services import AccountService

from .services import UserService
from .serializers import UserSerializer
# Create your views here.

filter = JwtFilter()

user_service = UserService()
account_service = AccountService()


@api_view(['POST', 'PUT'])
def handle(request: Request) -> JsonResponse:
    obj: str = 'user'
    # Post method
    if request.method == "POST":
        user: User = from_dict(Model=User, dictionary=request.data)
        account: Account = from_dict(Model=Account, dictionary=request.data)

        saved_user: User = user_service.add(user)
        if saved_user is None:
            return JsonResponse(APIResponse(message='Cannot add User', object=obj).to_json(), status=StatusCode.ERROR_SERVER)
        
        account.user_id = saved_user.id
        saved_account: Account = account_service.add(account)

        if saved_account is None:
            return JsonResponse(APIResponse(message='Cannot add Account', object=obj).to_json(), status=StatusCode.ERROR_SERVER)
        user_serializer = UserSerializer(saved_user)
        return JsonResponse(APIResponse(success=True, message='Registered User', object=obj, data=user_serializer.data).to_json(), status=StatusCode.OK)
    # PUT method
    elif request.method == "PUT":
        account_id: str = filter.get_account_id(request.headers.get('Authorization'))

        if account_id is None:
            return JsonResponse(APIResponse(success=False, message='Invalid Token', object=obj, data=None).to_json(), status=StatusCode.BAD_REQUEST)
        account: Account = account_service.get_by_id(account_id)
        print(account.__dict__)
        if account is None:
            return JsonResponse(APIResponse(success=False, message='Not found Account', object=obj, data=None).to_json(), status=StatusCode.NOT_FOUND)
        
        user: User = user_service.get_by_id(account.user_id)
        if user is None:
            return JsonResponse(APIResponse(success=False, message='Not found User', object=obj, data=None).to_json(), status=StatusCode.BAD_REQUEST)
        
        edit_data: User = map(from_obj=user, to_obj=User())
        edit_data = get_data(obj=edit_data, dictionary=request.data)

        edited_user: User = user_service.edit(user, edit_data)
        if edit_data is None:
            return JsonResponse(APIResponse(success=False, message='Internal Error Server', object=obj, data=None).to_json(), status=StatusCode.ERROR_SERVER)
        user_serializer = UserSerializer(edited_user)
        return JsonResponse(APIResponse(success=True, message='Edited User', object=obj, data=user_serializer.data).to_json(), status=StatusCode.OK)
        

@api_view(['GET'])
def auth(request: Request) -> JsonResponse:
    if request.method == 'GET':
        obj: str = 'user'
        account_id = filter.get_account_id(request.headers.get('Authorization'))

        if account_id is None:
            return JsonResponse(APIResponse(message='Invalid Token', object=obj).to_json(), status=StatusCode.BAD_REQUEST)
        
        account: Account = account_service.get_by_id(account_id)

        if account is None:
            return JsonResponse(APIResponse(message='Not found User', object=obj).to_json(), status=StatusCode.NOT_FOUND)
        
        user: User = user_service.get_by_id(account.user_id)
        if user is None:
            return JsonResponse(APIResponse(message='Internal Error Server', object=obj).to_json(), status=StatusCode.ERROR_SERVER)
        user_serializer = UserSerializer(user)

        return JsonResponse(APIResponse(success=True, message='Got User', object=obj, data=user_serializer.data).to_json(), status=StatusCode.OK)