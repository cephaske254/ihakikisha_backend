from django.shortcuts import render
from rest_framework import generics
from . import serializers
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import Distributor, User, Shop, Manufacturer, Farmer
# Create your views here.

class DistributorProfile(generics.ListCreateAPIView):
    serializer_class = serializers.DistributorProfileSerializer
    queryset = Distributor.objects.all()
    permission_classes = (IsAuthenticated)

class DistributorProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.DistributorProfileSerializer
    queryset = Distributor.objects.all()
    permission_classes = (IsAuthenticated)



class ManufacturerProfile(generics.ListCreateAPIView):
    serializer_class = serializers.ManufacturerProfileSerializer
    queryset = Manufacturer.objects.all()

class ManufacturerProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ManufacturerProfileSerializer
    queryset = Manufacturer.objects.all()
    permission_classes = (IsAuthenticated)


class FarmerProfile(generics.ListCreateAPIView):
    serializer_class = serializers.FarmerProfileSerializer
    queryset = Farmer.objects.all()
    permission_classes = (IsAuthenticated)

class FarmerProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.FarmerProfileSerializer
    queryset = Farmer.objects.all()
    permission_classes = (IsAuthenticated)
