from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import AllowAny
from .models import *

# Create your views here
class ProductSetDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSetSerializer
    queryset = ProductSet.objects.all()

class AddProductSet(generics.ListCreateAPIView):
    serializer_class = ProductSetSerializer
    queryset = ProductSet.objects.all()


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class AddProduct(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
