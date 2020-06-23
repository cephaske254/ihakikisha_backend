from rest_framework import serializers
from .models import *

class ProductSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSet
        fields = ('__all__')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')
