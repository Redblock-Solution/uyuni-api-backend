# users/urls.py
from django.urls import path
from .views import UserCreateView

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='user-create')
]
