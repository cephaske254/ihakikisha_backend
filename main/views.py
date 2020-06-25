from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.permissions import AllowAny
from . import serializers
from .models import Distributor, User, Shop, Manufacturer, Farmer, Rating, Package, ProductSet, Product

from rest_framework.permissions import AllowAny,IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.

class ProductSetDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProductSetSerializer
    queryset = ProductSet.objects.all()

class ProductSets(generics.ListCreateAPIView):
    serializer_class = serializers.ProductSetSerializer
    queryset = ProductSet.objects.all()
    

class Products(generics.ListCreateAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    permission_classes=(IsAuthenticatedOrReadOnly,)

class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()


class RetrieveProduct(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ProductRetrieveSerializer
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
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Rating.objects.all()

    def post(self, request, *args, **kwargs):
        request.data['user']=request.user.id
        return self.create(request, *args, **kwargs)

    

class RatingsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RatingsSerializer
    queryset = Rating.objects.all()
    

class Packages(generics.ListCreateAPIView):
    serializer_class = serializers.PackageSerializer
    queryset = Package.objects.all()
    
class PackageDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PackageSerializer
    queryset = Package.objects.all()
    

