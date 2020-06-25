from rest_framework import serializers
from .models import Distributor, Farmer, Manufacturer, Shop, Rating, Package, ProductSet, Product
from authentication.serializers import UserSerializerNano
from authentication.models import User
from cloudinary.models import CloudinaryField
from django.conf import settings


class ProductSetSerializer(serializers.ModelSerializer, ):
    class Meta:
        model = ProductSet
        fields = '__all__'

class ManufacturerSerializerMini(serializers.ModelSerializer,):

    class Meta:
        model = Manufacturer
        fields = ['name', 'phone', 'email', 'location', 'logo']


class ProductSetSerializerMini(serializers.ModelSerializer,):
    manufacturer = ManufacturerSerializerMini()

    class Meta:
        fields = ['name', 'description', 'composition', 'manufacturer']
        model = ProductSet


class ProductSerializer(serializers.ModelSerializer, ):

    class Meta:
        model = Product
        fields = '__all__'


class ProductRetrieveSerializer(serializers.ModelSerializer, ):
    class Meta:
        model = Product
        fields = ['uuid', 'manufactured', 'sold', 'qr_code', 'product_set']
        extra_kwargs = {"qr_code": {"read_only": True}}


class FarmerProfileSerializer(serializers.ModelSerializer, ):

    class Meta:
        model = Farmer
        exclude = []


class ManufacturerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        exclude = []


class DistributorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        exclude = []


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
