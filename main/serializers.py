from rest_framework import serializers
from .models import Shop, Package, Rating
from authentication.serializers import UserSerializerMini
from authentication.models import User

class ShopProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        exclude = []

class RatingsProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        exclude = []

class PackageProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        exclude = []

        