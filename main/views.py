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
    ordering=['ratings']
    filter_backends = [filters.OrderingFilter]


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

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

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
    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(manufacturer=user.id)


class MyProductsetsRating(generics.ListAPIView):
    def get(self, request, name):
        products = Rating.objects.filter(product_set__name=name).all()
        return Response (data = serializers.ProductsetsRatingSerializer(products, many=True).data)

class HighlightRating(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.RatingsHighlightSerializer
    queryset = Rating.objects.all()
    def get_queryset(self):
        id = self.kwargs['pk']
        return Rating.objects.filter(pk=id)

    def perform_update(self, serializer):
        if self.get_object().highlight == False:
            serializer.save(highlight=True)
        else:
            serializer.save(highlight=False)


class HiglightRatingList(generics.ListAPIView):
    serializer_class = serializers.ProductsetsRatingSerializer
    queryset = Rating.objects.all()
    def get_queryset(self):
        return self.queryset.filter(product_set__manufacturer_id=self.request.user.id, highlight=True)

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


class MyDistributors(generics.ListCreateAPIView):
    queryset = Farmer.objects.all()
    serializer_class = serializers.MyDistributorProfileSerializer
    
    def get_queryset(self):
        return self.queryset.filter(distrib__manufacturer=self.request.user.id)

class MyDistributorsAdd(generics.CreateAPIView):
    queryset = Distributor.objects.all()
    serializer_class = serializers.DistributorProfileSerializer
    
    def post(self, request, email, *args, **kwargs):
        user = Farmer.objects.filter(user__email=email).first()
        manufacturer = Manufacturer.objects.filter(pk=self.request.user.id).first()
        
        if user is not None and manufacturer is not None:
            exists = self.queryset.filter(user = user.pk).exists()
            if not exists:
                distributor = Distributor.objects.create(user=user, manufacturer=manufacturer).save()
                return Response(data=serializers.DistributorProfileSerializer(distributor).data, status=201)

        return Response(status=400, data={'non_field_errors':['Could not complete your request.Check if you provided a matching email']})
        
        


class SearchProducts(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer
    permission_classes = (AllowAny,)

    queryset = ProductSet.objects.all()
    search_fields = ['name', 'manufacturer__name', 'composition', 'description']
    filter_backends = (filters.SearchFilter,)
