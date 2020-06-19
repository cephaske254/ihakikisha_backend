from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password 

class UserSerializerMini(serializers.ModelSerializer):
    password_1 = serializers.CharField()
    class Meta:
        model = User
        fields = ['email', 'first_name','last_name','user_type','password','password_1']
        extra_kwargs = {
            'password': {
                'write_only': True, 'validators':[validate_password]
                },
            }

    def create(self, validated_data):
        validated_data.pop('password_1')
        user = User.objects.create_user(**validated_data)
        return user
