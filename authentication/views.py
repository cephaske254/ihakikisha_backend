from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import response, authtoken, mixins
from rest_framework.generics import CreateAPIView
from . import serializers
from authentication.models import User
from django.contrib.auth.password_validation import validate_password 


# Create your views here.
class Register(CreateAPIView):
    serializer_class = serializers.UserSerializerMini
    def validate(self, data):
        if validate_password(data.get('password')):
            return data

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
    


class CustomAuthToken(authtoken.views.ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return response.Response({
            'token': token.key,
            'uid': user.pk,
            'email': user.email,
            'user_type': user.user_type,
        })

