from rest_framework import serializers
from .models import Distributor,Farmer,Manufacturer
from authentication.serializers import UserSerializerNano
from authentication.models import User


class FarmerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        exclude =[]

class ManufacturerProfileSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Manufacturer
        exclude =[]

class DistributorProfileSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    user = UserSerializerNano(many=False)
    manufacturer = ManufacturerProfileSerializer(many=False)
    class Meta:
        model = Distributor
        exclude =[]
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

        
