from rest_framework import serializers
from .models import Shop, Package, Rating
from authentication.serializers import UserSerializerMini
from authentication.models import User

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        exclude = []

class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        exclude = []

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        exclude = []

        