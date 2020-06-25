from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password 
from django.contrib.auth import authenticate
from main.models import Distributor, Farmer, Manufacturer
class UserSerializerMini(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','uuid', 'first_name','last_name','user_type','password']

        extra_kwargs = {
            'password': {
                'write_only': True, 'validators':[validate_password]
                },
            }

            
        
class UserSerializerNano(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name','last_name','email']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class TokenSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=255, write_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(email=email, password=password)
        return user
