from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import AllowAny
from .models import *

# Create your views here
class AddProductSet(generics.CreateAPIView):
    serializer_class = ProductSetSerializer
    queryset = ProductSet.objects.all()

class DeleteProductSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSetSerializer
    queryset = ProductSet.objects.all()

class UpdateProductSet(generics.RetrieveUpdateAPIView):
    serializer_class = ProductSetSerializer
    queryset = ProductSet.objects.all()

class AllProductSets(generics.ListCreateAPIView):
    serializer_class = ProductSetSerializer
    queryset = ProductSet.objects.all()

class GetProductSet(generics.RetrieveAPIView):
    serializer_class = ProductSetSerializer
    queryset = ProductSet.objects.all()

class UpdateProduct(generics.RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class GetProduct(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class AllProducts(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
