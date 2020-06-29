from rest_framework import serializers
from .models import Distributor, Farmer, Manufacturer, Shop, Rating, Package, ProductSet, Product
from authentication.serializers import UserSerializerNano
from authentication.models import User
from cloudinary.models import CloudinaryField
from django.core import serializers as django_serializer

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
        fields = ['name', 'description', 'composition', 'manufacturer', 'image']
        model = ProductSet


class ProductSerializer(serializers.ModelSerializer, ):

    class Meta:
        model = Product
        fields = '__all__'


class ProductRetrieveSerializer(serializers.ModelSerializer, ):
    product_set = ProductSetSerializerMini()
    class Meta:
        model = Product
        fields = ['id', 'uuid', 'manufactured', 'sold', 'qr_code', 'product_set',]
        extra_kwargs = {"qr_code": {"read_only": True}}


class FarmerProfileSerializer(serializers.ModelSerializer, ):

    class Meta:
        model = Farmer
        exclude = []


class ManufacturerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        exclude = []


class DistributorProfileSerializerMini(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        exclude = []
        extra_kwargs = {
            'manufacturer': {'required': False},
            'user': {'required': False,},
            }


class DistributorProfileSerializer(serializers.ModelSerializer):
    user = UserSerializerNano()
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


class ProfileSerializer(serializers.ModelSerializer):
    company_profile = serializers.SerializerMethodField()
    product_sets = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    distributors = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'user_type', 'company_profile', 'products','product_sets','distributors']

    def get_company_profile(self, obj):
        if obj.user_type == 'M':
            query_set = Manufacturer.objects.get(pk=obj.pk)
            return ManufacturerProfileSerializer(query_set, many=False).data

        elif obj.user_type == 'D':
            query_set = Distributor.objects.get(pk=obj.pk)
            return DistributorProfileSerializerMini(query_set, many=False).data

        if obj.user_type == 'F':
            query_set = Farmer.objects.get(pk=obj.pk)
            return FarmerProfileSerializer(query_set, many=False).data

    def get_products(self, obj):
        query_set = Product.objects.filter(product_set__manufacturer__user=obj.pk).count()
        return query_set
    
    def get_product_sets(self, obj):
        query_set = ProductSet.objects.filter(manufacturer__user=obj.pk).count()
        return query_set

    def get_distributors(self, obj):
        query_set = Distributor.objects.filter(manufacturer=obj.pk).count()
        return query_set