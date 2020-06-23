from django.shortcuts import render
from rest_framework import generics
from . import serializers
from rest_framework.permissions import AllowAny
from .models import Shop, Package, Rating

# Create your views here.

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
    


