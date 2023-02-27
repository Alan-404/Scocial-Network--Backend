from .models import Post
from .serializers import PostSerializer
from django.utils import timezone
from utils.lib import make_id
from utils.constants import length_id

class PostService:
    def __init__(self) -> None:
        self.model = Post
        self.serializer = PostSerializer

    def add(self, post: Post) -> Post:
        try:
            post.id = make_id(length_id)
            post.created_at = timezone.now()
            post.modified_at = timezone.now()
            print(post.__dict__)
            post_serializer = self.serializer(data=post.__dict__)
            if post_serializer.is_valid():
                post_serializer.save()
                return post
            else:
                print(post_serializer.errors)
                return None
        except Exception as e:
            print(e)
            return None
        
    def edit(self, post: Post, edit_data: Post) -> Post:
        try:
            edit_data.modified_at = timezone.now()

            post_serializer = self.serializer(post, data=edit_data.__dict__)
            if post_serializer.is_valid():
                post_serializer.save()
                return edit_data
            return None
        except Exception as e:
            return None