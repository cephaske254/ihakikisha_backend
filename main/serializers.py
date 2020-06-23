from rest_framework import serializers
from .models import Distributor,Farmer,Manufacturer, Shop, Rating, Package
from authentication.serializers import UserSerializerNano
from authentication.models import User


class FarmerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        exclude =[]

class ManufacturerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        exclude =[]

class DistributorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        exclude =[]

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
