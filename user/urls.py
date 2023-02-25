from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.register_user)
]