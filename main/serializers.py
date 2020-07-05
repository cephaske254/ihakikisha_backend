from rest_framework import serializers
from .models import Distributor, Farmer, Manufacturer, Shop, Rating, Package, ProductSet, Product
from authentication.serializers import UserSerializerNano, UserSerializerMini
from authentication.models import User
from cloudinary.models import CloudinaryField
from django.core import serializers as django_serializer

from statistics import mean

class ManufacturerSerializerMini(serializers.ModelSerializer,):

    class Meta:
        model = Manufacturer
        fields = ['name', 'phone', 'email', 'location', 'logo']

class ManufacturerStatsSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    distributor_count = serializers.SerializerMethodField()
    product_set_count = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    date_joined = serializers.SerializerMethodField()
    class Meta:
        model = Manufacturer
        fields = ['products_count','distributor_count','product_set_count','reviews_count','date_joined']

    def get_products_count(self, obj):
        return Product.objects.filter(product_set__manufacturer__pk=obj.pk).count()

    def get_distributor_count(self, obj):
        return Distributor.objects.filter(manufacturer=obj.pk).count()

    def get_product_set_count(self, obj):
        return ProductSet.objects.filter(manufacturer=obj.pk).count()

    def get_reviews_count(self, obj):
        return Rating.objects.filter(product_set__manufacturer=obj.pk).count()

    def get_date_joined(self, obj):
        return User.objects.get(pk=obj.pk).date_joined


class ProductSetSerializerDetail(serializers.ModelSerializer, ):
    manufacturer = ManufacturerSerializerMini()
    class Meta:
        model = ProductSet
        exclude = []

class ProductSetSerializerMini(serializers.ModelSerializer,):
    manufacturer = ManufacturerSerializerMini()

    class Meta:
        fields = ['id','name', 'description', 'composition', 'manufacturer', 'image']
        model = ProductSet


class ProductSerializer(serializers.ModelSerializer, ):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs={
            'product_set':{'required':True},
            'manufactured':{'required':True},
            'expires':{'required':True},
        }


class ProductsetsRatingSerializer(serializers.ModelSerializer):
    user = UserSerializerNano()
    avatar = serializers.SerializerMethodField()
    product_set = ProductSetSerializerMini()
    class Meta:
        model = Rating
        fields = '__all__'
    
    def get_avatar(self, obj):
        try:
             return str(Farmer.objects.get(user=obj.user).image)
        except:
            return str(Manufacturer.objects.get(pk=obj.user).logo)


class ProductSetSerializer(serializers.ModelSerializer, ):
    manufacturer = ManufacturerSerializerMini(read_only=True)
    review_count = serializers.SerializerMethodField()
    review_average = serializers.SerializerMethodField()
    class Meta:
        model = ProductSet
        fields = '__all__'
        extra_kwargs={
            'manufacturer':{'required':False}
        }


    def get_review_count(self, obj):
        return Rating.objects.filter(product_set=obj.pk).count()

    def get_review_average(self, obj):
        reviews = Rating.objects.filter(product_set=obj.pk).all()
        numbers = [item.rating for item in reviews] or [0]
        return round(mean(numbers),2)


class ProductBulkSerializer(serializers.ModelSerializer, ):
    class Meta:
        model = Product
        fields = '__all__'


class ProductRetrieveSerializer(serializers.ModelSerializer, ):
    product_set = ProductSetSerializerMini()
    class Meta:
        model = Product
        fields = ['id', 'uuid', 'manufactured', 'sold', 'qr_code', 'product_set',]
        extra_kwargs = {"qr_code": {"read_only": True}}


class FarmerProfileSerializer(serializers.ModelSerializer, ):
    class Meta:
        model = Farmer
        exclude = []


class ManufacturerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        exclude = []
        extra_kwargs = {
            'user': {'required': False,},
            }


class DistributorProfileSerializerMini(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        exclude = []
        extra_kwargs = {
            'manufacturer': {'required': False},
            'user': {'required': False,},
            }            


class MyDistributorProfileSerializer(serializers.ModelSerializer):
    user = UserSerializerNano()
    class Meta:
        model = Farmer
        exclude = []
        


class DistributorProfileSerializer(serializers.ModelSerializer):
    user = UserSerializerNano(read_only=True)
    class Meta:
        model = Distributor
        exclude = []
        extra_kwargs={
            'manufacturer':{'required':False}
        }


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        exclude = []


class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        exclude = []
        extra_kwargs={
            'user':{'required':False}
        }

class RatingsHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        exclude = []
        extra_kwargs={
            'user':{'read_only':True},
            'rating':{'read_only':True},
            'product_set':{'read_only':True},
            'comment':{'read_only':True},
        }

class RatingsDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rating
        fields = ['id', 'rating', 'comment', 'product_set','user']

class RatingsStatsSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()
    null_comment_count = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    review_sum = serializers.SerializerMethodField()
    review_average = serializers.SerializerMethodField()
    product_set = serializers.SerializerMethodField()

    class Meta:
        model = ProductSet
        fields=['comment_count','null_comment_count','review_count','review_sum','review_average','product_set']

    def get_comment_count(self, obj):
        return Rating.objects.filter(product_set=obj.pk, comment__isnull=False).count()

    def get_null_comment_count(self, obj):
        return Rating.objects.filter(product_set=obj.pk, comment__isnull=True).count()

    def get_review_count(self, obj):
        return Rating.objects.filter(product_set=obj.pk).count()

    def get_review_sum(self, obj):
        reviews = Rating.objects.filter(product_set=obj.pk).all()
        numbers = [item.rating for item in reviews] or [0]
        return sum(numbers)

    def get_review_average(self, obj):
        reviews = Rating.objects.filter(product_set=obj.pk).all()
        numbers = [item.rating for item in reviews] or [0]
        return round(mean(numbers),2)

    def get_product_set(self, obj):
        return ProductSetSerializer(ProductSet.objects.get(pk=obj.id)).data
            


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        exclude = []


class ProfileSerializer(serializers.ModelSerializer):
    company_profile = serializers.SerializerMethodField()
    product_sets = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    distributors = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'user_type', 'company_profile', 'products','product_sets','distributors']

    def get_company_profile(self, obj):
        if obj.user_type == 'M':
            query_set = Manufacturer.objects.get(pk=obj.pk)
            return ManufacturerProfileSerializer(query_set, many=False).data

        elif obj.user_type == 'D':
            query_set = Distributor.objects.get(pk=obj.pk)
            return DistributorProfileSerializerMini(query_set, many=False).data

        if obj.user_type == 'F':
            query_set = Farmer.objects.get(pk=obj.pk)
            return FarmerProfileSerializer(query_set, many=False).data

    def get_products(self, obj):
        query_set = Product.objects.filter(product_set__manufacturer__user=obj.pk).count()
        return query_set
    
    def get_product_sets(self, obj):
        query_set = ProductSet.objects.filter(manufacturer__user=obj.pk).count()
        return query_set

    def get_distributors(self, obj):
        query_set = Distributor.objects.filter(manufacturer=obj.pk).count()
        return query_set