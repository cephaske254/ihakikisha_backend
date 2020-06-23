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