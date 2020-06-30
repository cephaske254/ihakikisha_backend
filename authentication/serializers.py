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
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            if not user:
                msg = ('Credentials Doesnt Match Our Records!')
                raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs

