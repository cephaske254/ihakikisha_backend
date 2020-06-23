from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import AllowAny
from .models import *
from . import serializers
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import Distributor, User, Shop, Manufacturer, Farmer, Rating, Package

# Create your views here
class ProductSetDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSetSerializer
    queryset = ProductSet.objects.all()

class ProductSets(generics.ListCreateAPIView):
    serializer_class = ProductSetSerializer
    queryset = ProductSet.objects.all()


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    
class Products(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    

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
    

