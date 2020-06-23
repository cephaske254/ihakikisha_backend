from django.shortcuts import render
from rest_framework import generics
from . import serializers
from rest_framework.permissions import AllowAny
from .models import Shop, Package, Rating

# Create your views here.

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
    


