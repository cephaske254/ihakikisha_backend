from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import response, authtoken, mixins
from rest_framework import generics
from rest_framework .views import APIView
from . import serializers
from authentication.models import User
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication
from rest_framework.authtoken.models import Token
from django.core.exceptions import PermissionDenied
from rest_framework.status import HTTP_401_UNAUTHORIZED


from rest_framework import parsers, renderers

# Create your views here.


class Register(generics.CreateAPIView):
    serializer_class = serializers.UserSerializerMini
    permission_classes = (AllowAny,)
    authentication_classes =(BasicAuthentication,)


class CustomAuthToken(authtoken.views.ObtainAuthToken):
    serializer_class = serializers.TokenSerializer
    permission_classes = (AllowAny,)
    authentication_classes =(BasicAuthentication,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return response.Response({'token': token.key, 'user_id':user.pk, 'user_type':user.user_type, 'email':user.email})