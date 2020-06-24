from rest_framework import serializers
from .models import Distributor,Farmer,Manufacturer, Shop, Rating, Package, ProductSet, Product
from authentication.serializers import UserSerializerNano
from authentication.models import User

class ProductSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSet
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {"qr_code":{"read_only":True}}
        


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
