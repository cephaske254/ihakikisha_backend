from django.shortcuts import render
from rest_framework import generics
from . import serializers
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import Distributor, User, Shop, Manufacturer, Farmer, Rating, Package
# Create your views here.

class DistributorProfile(generics.ListCreateAPIView):
    serializer_class = serializers.DistributorProfileSerializer
    queryset = Distributor.objects.all()
    permission_classes = (IsAuthenticated,)

class DistributorProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.DistributorProfileSerializer
    queryset = Distributor.objects.all()
    permission_classes = (IsAuthenticated,)



class ManufacturerProfile(generics.ListCreateAPIView):
    serializer_class = serializers.ManufacturerProfileSerializer
    queryset = Manufacturer.objects.all()
    permission_classes = (IsAuthenticated,)

class ManufacturerProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ManufacturerProfileSerializer
    queryset = Manufacturer.objects.all()
    permission_classes = (IsAuthenticated,)


class FarmerProfile(generics.ListCreateAPIView):
    serializer_class = serializers.FarmerProfileSerializer
    queryset = Farmer.objects.all()
    permission_classes = (IsAuthenticated,)

class FarmerProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.FarmerProfileSerializer
    queryset = Farmer.objects.all()
    permission_classes = (IsAuthenticated,)

    
class ShopProfile(generics.ListCreateAPIView):
    serializer_class = serializers.ShopProfileSerializer
    queryset = Shop.objects.all()


class ShopProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ShopProfileSerializer
    queryset = Shop.objects.all()

class RatingsProfile(generics.ListCreateAPIView):
    serializer_class = serializers.RatingsProfileSerializer
    queryset = Rating.objects.all()

class RatingsProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RatingsProfileSerializer
    queryset = Rating.objects.all()

class PackageProfile(generics.ListCreateAPIView):
    serializer_class = serializers.PackageProfileSerializer
    queryset = Package.objects.all()

class PackageProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PackageProfileSerializer
    queryset = Package.objects.all()
    


