from django.http import JsonResponse
from rest_framework.decorators import api_view
from utils.lib import from_dict, model_to_dict
from .services import PostService
from rest_framework.request import Request
from utils.enums import StatusCode, RequestMethod, HeaderOption
from .models import Post
from utils.middle_ware import JwtFilter
from utils.dtos import APIResponse
from user.services import UserService
from account.services import AccountService
from .serializers import PostSerializer
# Create your views here.

filter = JwtFilter()

post_service = PostService()
account_service = AccountService()
user_service = UserService()


@api_view([RequestMethod.POST_METHOD.value, RequestMethod.PUT_METHOD.value])
def handle(request: Request):
    if request.method == RequestMethod.POST_METHOD.value:
        account_id: str = filter.get_account_id(request.headers.get(HeaderOption.AUTHORIZATION.value))
        if account_id is None:
            return JsonResponse(APIResponse(message='Invalid Token').to_json(), status=StatusCode.BAD_REQUEST)
        account = account_service.get_by_id(account_id)
        if account is None:
            return JsonResponse(APIResponse(message='Invalid Token').to_json(), status=StatusCode.BAD_REQUEST)
        
        post_data: Post = from_dict(Model=Post, dictionary=request.data)
        post_data.user_id = account.user_id
        saved_post: Post = post_service.add(post_data)
        if saved_post is None:
            return JsonResponse(APIResponse(message='Internal Error Server').to_json(), status=StatusCode.ERROR_SERVER)
        post_serializer = PostSerializer(saved_post)
        return JsonResponse(APIResponse(success=True, message='Saved Post', object='post', data=post_serializer.data).to_json(), status=StatusCode.OK)
    elif request.method == RequestMethod.PUT_METHOD.value:
        account_id = filter.get_account_id(request.headers.get(HeaderOption.AUTHORIZATION.value))
        if account_id is None:
            return JsonResponse(APIResponse(message='Invalid Token').to_json(), status=StatusCode.BAD_REQUEST)
        
        account = account_service.get_by_id(account_id)
        if account is None:
            return JsonResponse(APIResponse(message='Invalid Token').to_json(), status=StatusCode.BAD_REQUEST)
        






