from django.shortcuts import render
from rest_framework import generics,mixins, response
from main.models import User
from .serializers import UserSerializer
# Create your views here.
class RegisterUser(generics.CreateAPIView,mixins.CreateModelMixin):
    '''
        /api/register/  [POST] only
        password, email, first_name, last_name
    '''
    serializer_class = UserSerializer
