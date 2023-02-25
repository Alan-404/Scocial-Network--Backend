from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request

from .models import Account

from .business import AccountBusiness
from .dtos import LoginResponse

from utils.middle_ware import JwtFilter

# Create your views here.

business = AccountBusiness()
filter = JwtFilter()

@api_view(['POST'])
def auth(request: Request) -> JsonResponse:
    account: Account = business.login(request.data)
    if account:
        token = filter.generate_access_token(account.id)
        return JsonResponse(LoginResponse(success=True, message="Successfully", access_token=token).to_dict())
    else:
        return JsonResponse({'success': False})
