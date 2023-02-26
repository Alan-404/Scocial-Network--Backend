from django.urls import path
from . import views



urlpatterns = [
    path("", views.handle),
    path('info', views.auth)
]