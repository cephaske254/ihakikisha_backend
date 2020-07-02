from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.permissions import AllowAny
from . import serializers
from .models import Distributor, User, Shop, Manufacturer, Farmer, Rating, Package, ProductSet, Product

from rest_framework.permissions import AllowAny,IsAuthenticated, IsAuthenticatedOrReadOnly

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from rest_framework import filters
# Create your views here.

class ProductSetDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProductSetSerializer
    permission_classes=(IsAuthenticatedOrReadOnly,)
    queryset = ProductSet.objects.all()

class ProductSets(generics.ListCreateAPIView):
    serializer_class = serializers.ProductSetSerializer
    permission_classes=(IsAuthenticatedOrReadOnly,)
    queryset = ProductSet.objects.all()
    
    def perform_create(self, serializer):
        manufacturer = Manufacturer.objects.get(pk=self.request.user.id)
        serializer.save(manufacturer=manufacturer)
    

class Products(generics.ListCreateAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    permission_classes=(IsAuthenticatedOrReadOnly,)

class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()

class CreateBulkProducts(generics.CreateAPIView):
    serializer_class = serializers.ProductBulkSerializer
    queryset = Product.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data[0])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        serializer.save(product_set=ProductSet.objects.get(name=self.request.data[0].get('product_set_name')))


class RetrieveProduct(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ProductRetrieveSerializer
    lookup_field = 'uuid'
    queryset = Product.objects.all()
           

class DistributorProfile(generics.ListCreateAPIView):
    serializer_class = serializers.DistributorProfileSerializerMini
    queryset = Distributor.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        

class DistributorProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.DistributorProfileSerializerMini
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

class ManufacturerStats(generics.ListAPIView):
    serializer_class = serializers.ManufacturerStatsSerializer
    queryset = Manufacturer.objects.all()

    def get_queryset(self):
        manufacturer = self.request.user.id
        return Manufacturer.objects.filter(pk=manufacturer)


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
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RatingsDetail(generics.ListAPIView):
    serializer_class = serializers.RatingsDetailSerializer
    queryset = Rating.objects.all()
    permission_classes = (AllowAny,)

    def get_queryset(self):
        id = self.kwargs['product_set_id']
        return Rating.objects.filter(product_set=id)



class RatingsStats(generics.ListAPIView):
    serializer_class = serializers.RatingsStatsSerializer
    queryset = Rating.objects.all()
    permission_classes = (AllowAny,)

    def get_queryset(self):
        id = self.kwargs['product_set_id']
        return ProductSet.objects.filter(pk=id)

class Packages(generics.ListAPIView):
    serializer_class = serializers.PackageSerializer
    queryset = Package.objects.all()
    
class PackageDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PackageSerializer
    queryset = Package.objects.all()
    

class Profile(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ProfileSerializer
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        obj = get_object_or_404(queryset,id=self.request.user.id)
        return obj

class MyProductsets(generics.ListCreateAPIView):
    queryset = ProductSet.objects.all()
    serializer_class = serializers.ProductSetSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        obj = get_object_or_404(queryset,manufacturer=self.request.user.id)
        return obj

class MyProductsetsDetail(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    def get(self, request, name):
        products = Product.objects.filter(product_set__name=name).all()
        return Response (data = serializers.ProductSerializer(products, many=True).data)
        


class MyProducts(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        obj = get_object_or_404(queryset,product_set__manufacturer=self.request.user.id)
        return obj


class MyDistributors(generics.ListAPIView):
    queryset = Distributor.objects.all()
    serializer_class = serializers.DistributorProfileSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        obj = get_object_or_404(queryset,manufacturer=self.request.user.id)
        return obj


class SearchProducts(generics.ListAPIView):
    serializer_class = serializers.ProductSetSerializerDetail
    permission_classes = (AllowAny,)
    

    queryset = ProductSet.objects.all()
    search_fields = ['name', 'manufacturer__name', 'composition', 'description']
    filter_backends = (filters.SearchFilter,)
