from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.permissions import AllowAny
from . import serializers
from .models import Distributor, User, Shop, Manufacturer, Farmer, Rating, Package, ProductSet, Product

from rest_framework.permissions import AllowAny,IsAuthenticated, IsAuthenticatedOrReadOnly

from django.shortcuts import get_object_or_404
from rest_framework.response import Response

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
    serializer_class = serializers.DistributorProfileSerializerMini
    queryset = Distributor.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get_by_natural_key(email=request.POST['email'])
        except:
            return Response(status=404, data={'non_field_errors':{'User Not Found!'}})
        manufacturer = Manufacturer.objects.get(pk=request.user.pk)
        try:
            distributor = Distributor.objects.create(user=user, manufacturer=manufacturer)
        except:
            return Response(status=400, data={'non_field_errors':{'Distributor already registered!'}})
        return Response(status=404, data=distributor)
        

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
    serializer_class = serializers.ProductSetSerializer
    permission_classes = (AllowAny,)

    queryset = ProductSet.objects.all()
    search_fields = ['name', 'manufacturer__name', 'composition', 'description']
    filter_backends = (filters.SearchFilter,)
