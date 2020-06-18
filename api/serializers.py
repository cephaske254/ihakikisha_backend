from rest_framework import serializers, validators
from main.models import User
from django.contrib.auth.password_validation import validate_password
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'first_name':{'required': True},
            'last_name': {'required': True},
            'password': {'validators': [validate_password]},
        }

