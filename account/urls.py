from django.urls import path
from . import views

urlpatterns = [
    path('auth', view=views.auth)
]