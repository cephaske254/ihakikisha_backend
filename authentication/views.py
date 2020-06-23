from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import response, authtoken, mixins
from rest_framework import generics
from rest_framework .views import APIView
from . import serializers
from authentication.models import User
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.core.exceptions import PermissionDenied
from rest_framework.status import HTTP_401_UNAUTHORIZED

# Create your views here.


class Register(generics.CreateAPIView):
    serializer_class = serializers.UserSerializerMini
    permission_classes = (AllowAny,)

class CustomAuthToken(authtoken.views.ObtainAuthToken):
    serializer_class = serializers.TokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return response.Response({
                'token': token.key,
                'uuid': user.uuid,
                'email': user.email,
                'user_type': user.user_type,
            })
        except:
            return response.Response({"status":HTTP_401_UNAUTHORIZED, "detail":"Password or Email Invalid!"})
