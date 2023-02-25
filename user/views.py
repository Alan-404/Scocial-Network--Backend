from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from .business import UserBusiness
from .dtos import RegisterResponse
from utils.middle_ware import JwtFilter
from utils.lib import model_to_dict
# Create your views here.

business = UserBusiness()
filter = JwtFilter()


@api_view(['POST'])
def register_user(request: Request) -> JsonResponse:
    saved_user = business.register_user(request.data)
    if saved_user is None:
        return JsonResponse({
            'success': False
        })
    return JsonResponse(model_to_dict(saved_user))

@api_view(['GET'])
def auth(request: Request) -> JsonResponse:
    print(request.__dict__)
    print(type(request))
    if request.method == 'GET':
        account_id = filter.get_account_id(token=request.headers.get('Authorization'))
        if account_id is None:
            return JsonResponse({'user': None})
        user = business.get_by_account_id(account_id)

        if user is None:
            return JsonResponse({'user': None})
        return JsonResponse({'user': model_to_dict(user)})