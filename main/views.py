from django.shortcuts import render
from rest_framework import generics, views
from .serializers import *
from rest_framework.permissions import AllowAny
from . import serializers
from rest_framework.permissions import AllowAny,IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Distributor, User, Shop, Manufacturer, Farmer, Rating, Package
from .permissions import IsOwner
from django.http import JsonResponse

# Create your views here.

class ProductSetDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSetSerializer
    queryset = ProductSet.objects.all()

class ProductSets(generics.ListCreateAPIView):
    serializer_class = ProductSetSerializer
    queryset = ProductSet.objects.all()
    

class Products(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class RetrieveProduct(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    serializer_class.Meta.depth=2
    lookup_field = 'uuid'
    queryset = Product.objects.all()
           


class DistributorProfile(generics.ListCreateAPIView):
    serializer_class = serializers.DistributorProfileSerializer
    queryset = Distributor.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

class DistributorProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.DistributorProfileSerializer
    queryset = Distributor.objects.all()
    permission_classes = (IsAuthenticated,)
    
class ManufacturerProfile(generics.ListCreateAPIView):
    serializer_class = serializers.ManufacturerProfileSerializer
    queryset = Manufacturer.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

class ManufacturerProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ManufacturerProfileSerializer
    queryset = Manufacturer.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class FarmerProfile(generics.ListCreateAPIView):
    serializer_class = serializers.FarmerProfileSerializer
    queryset = Farmer.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

class FarmerProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.FarmerProfileSerializer
    queryset = Farmer.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

class Shops(generics.ListCreateAPIView):
    serializer_class = serializers.ShopSerializer
    queryset = Shop.objects.all()


class ShopsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ShopSerializer
    queryset = Shop.objects.all()
    

class Ratings(generics.ListCreateAPIView):
    serializer_class = serializers.RatingsSerializer
    queryset = Rating.objects.all()
    

class RatingsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RatingsSerializer
    queryset = Rating.objects.all()
    

class Packages(generics.ListCreateAPIView):
    serializer_class = serializers.PackageSerializer
    queryset = Package.objects.all()
    

class PackageDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PackageSerializer
    queryset = Package.objects.all()
    

