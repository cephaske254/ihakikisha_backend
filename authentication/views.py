from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import response, authtoken, mixins
from rest_framework import generics
from rest_framework .views import APIView
from . import serializers
from authentication.models import User
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
# Create your views here.
class Register(generics.CreateAPIView):
    serializer_class = serializers.UserSerializerMini
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(status=200)

class UpdateUser(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.UserSerializerMini
    permission_classes = (AllowAny,)
    queryset = User.objects.all()


class CustomAuthToken(authtoken.views.ObtainAuthToken):
    serializer_class = serializers.TokenSerializer
    
    def post(self, request, *args, **kwargs):
        # serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer = self.serializer_class(data=request.data, context={'request':request})
        # import pdb; pdb.set_trace()

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return response.Response({
            'token': token.key,
            'uid': user.pk,
            'email': user.email,
            'user_type': user.user_type,
        })
