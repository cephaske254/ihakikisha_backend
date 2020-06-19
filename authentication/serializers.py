from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password 


class UserSerializerMini(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name','last_name','user_type','password']
        extra_kwargs = {
            'password': {
                'write_only': True, 'validators':[validate_password]
                },
            }
