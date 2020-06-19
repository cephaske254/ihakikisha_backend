from django.db import models
from utils.models import BaseAbstractModel
import statistics
from authentication.models import User
from django.db.models import Q

class Farmer(BaseAbstractModel):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    image = models.ImageField(upload_to='profiles/farmer',default='avatar.png')
    
    @classmethod
    def add_farmer(cls, user, image):
        profile = cls.objects.create(user=user, image=image).save()
        return profile

class Manufacturer(BaseAbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=255, null=False,blank=False)
    phone = models.IntegerField(blank=False, null=False)
    location = models.CharField(max_length=255, null=False,blank=False)
    email = models.EmailField(max_length=255)
    logo = models.ImageField(upload_to='profiles/manufacturer',default='avatar.png')

    def __str__(self):
        return 'Manufacturer - %s %s'%(self.name, self.email)
    
    @classmethod
    def add_manufacturer(cls, name, phone, location, email, logo):
        manufacturer = cls.objects.create(name=name, phone=phone, location=location, email=email, logo=logo)
        manufacturer.save()
        return manufacturer

    @classmethod
    def edit_manufacturer(cls,manufactuer_id, name, phone, location, email, logo):
        manufacturer = cls.get_manufacturer_by_id(manufactuer_id)
        manufacturer.name = name or manufacturer.name
        manufacturer.phone = phone or manufacturer.phone
        manufacturer.location = location or manufacturer.location
        manufacturer.email = email or manufacturer.email
        manufacturer.save()
        return manufacturer

    @classmethod
    def get_manufacturer_by_id(cls,manufactuer_id):
        manufacturer = cls.objects.get(pk=manufactuer_id)
        return manufacturer

class Distributor(BaseAbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    manufacturer = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer')
    image = models.ImageField(upload_to='profiles/distributor',default='avatar.png')

    @classmethod
    def save_distributor(cls,user,manufacturer,image):
        distributor = cls(user=user,manufacturer=manufacturer,image=image)
        distributor.save()
        return distributor

    @classmethod
    def get_distributor_by_id(cls,distributor_id):
        distributor = cls.objects.get(pk=distributor_id)
        return distributor

    @classmethod
    def update_distributor(cls,distributor_id,manufacturer,image):
        distributor = cls.get_distributor_by_id(distributor_id) #user field
        distributor.manufacturer = manufacturer or distributor.manufacturer
        distributor.image = image or distributor.image
        distributor.save()
        return distributor

    @classmethod
    def get_manufacturer_distributor(cls,manufacturer_id):
        distributors = cls.objects.filter(manufacturer=manufacturer_id).all()
        return distributors

    @classmethod
    def remove_distributor(cls,distributor_id):
        distributor = cls.get_distributor_by_id(distributor_id)
        user_id = distributor.user
        user = User.objects.get(pk=distributor_id)
        user.user_type = 'F'
        user.save()
        distributor.delete()

class ProductSet(models.Model):
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False,blank=False)
    composition = models.TextField(null=False,blank=False)
    image = models.ImageField(upload_to='products',null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s by %s'%(self.name,self.manufacturer.user.profile.name)

    @classmethod
    def create_product_set(cls,manufacturer,name,description,composition, image):
        product_set = cls.objects.create(manufacturer=manufacturer, name=name, description=description, composition=composition, image=image)
        product_set.save()
        return product_set

    @classmethod
    def update_product_set(cls,product_set_id, name, description, composition, image):
        product_set = cls.get_product_set_by_id(product_set_id)
        product_set.name = name or product_set.name
        product_set.composition = composition or product_set.composition
        product_set.description = sold or product_set.description
        product_set.image = date or product_set.image
        product.save()
        return product_set

    @classmethod
    def delete_product_set(cls,product_id):
        product_set = cls.get_product_set_by_id(product_id)
        product_set.delete()

    @classmethod
    def get_all(cls):
        product_sets = cls.objects.all()
        return product_sets

    @classmethod
    def get_product_set_by_id(cls,product_id):
        product_set = cls.objects.get(pk=product_id)
        return product_set


class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    manufactured = models.DateField()
    product_set = models.ForeignKey(ProductSet,on_delete=models.CASCADE)
    qr_code = models.CharField(max_length=500)
    sold = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def average_rating(self):
        product_id = self.id
        raw_ratings = Rating.get_products_rating(self.id)
        rating = round(statistics.mean(raw_ratings),1)
        return rating

    @classmethod
    def create_product(cls,name,manufactured,product_set_id,qr_code):
        product_set = ProductSet.get_product_set_by_id(product_set_id)

        product = cls(name=name,manufacured=manufacured,product_set=product_set,qr_code=qr_code)
        product.save()
        return product
    
    @classmethod
    def create_product(cls,name,manufactured,product_set_id,qr_code,date):
        product_set = ProductSet.get_product_set_by_id(product_set_id)
        product = cls(name=name,manufacured=manufacured,product_set=product_set,qr_code=qr_code,date=date)
        product.save()
        return product

    @classmethod
    def update_product(cls,product_id, name, manufactured, qr_code):
        product_set = ProductSet.get_product_set_by_id(product_set_id)
        product = cls.get_product_by_id(product_id)

        product.name = name or product.name
        product.manufactured = manufactured or product.manufactured
        product.qr_code = qr_code or product.qr_code
        product.save()
        return product

    @classmethod
    def set_as_sold(cls, product_id):
        product = cls.get_product_by_id(product_id)
        product.sold = True
        product.save()
        return product

    @classmethod
    def get_all_products(cls):
        products = cls.objects.all()
        return products

    @classmethod
    def delete_product(cls,id):
        product = cls.objects.get(id=id)
        product.delete()

    @classmethod
    def get_product_by_id(cls,id):
        product = cls.objects.get(id=id)
        return product

    @classmethod
    def check_if_sold(cls, id):
        product = cls.get_product_by_id(id)
        if product.sold == True:
            return True
        else:
            False
        
    @classmethod
    def update_product(cls,product_id, name, manufactured, qr_code):
        product = cls.get_product_by_id(product_id)
        product.name = name or product.name
        product.manufactured = manufactured or product.manufactured
        product.qr_code = qr_code or product.qr_code
        product.save()
        return product

    @classmethod
    def delete_product(cls,id):
        product = cls.objects.get(id=id)
        product.delete()

    @classmethod
    def get_all_products(cls):
        products = cls.objects.all()
        return products

    @classmethod
    def get_product_by_id(cls,id):
        product = cls.objects.get(id=id)
        return product

    @classmethod
    def search_products(cls, keywords):
        products = cls.objects.filter(
        Q(name__icontains=keywords) |
        Q(product_set__name__icontains = keywords) |
        Q(product_set__manufacturer__name__icontains = keywords) |
        Q(product_set__name__icontains = keywords))
        
        return products


class Shop(models.Model):
    name = models.CharField(max_length=255, null=False,blank=False, unique=True)
    phone = models.IntegerField(blank=False, null=False, unique=True)
    location = models.CharField(max_length=255, null=False,blank=False)
    email = models.EmailField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        unique_together=(('name','phone','location'),('name','location'))
    
    @classmethod
    def add_shop(cls, name, phone, location, email):
        shop = cls.objects.create(name=name,phone=phone, location=location, email=email, description=description)
        shop.save()
        return shop

    @classmethod
    def edit_shop(cls,shop_id, name, phone, location, email):
        shop = cls.get_shop_by_id(shop_id)
        shop.name = name or shop.name
        shop.phone = phone or shop.phone
        shop.location = location or shop.location
        shop.email = email or shop.email
        shop.save()
        return shop

    @classmethod
    def get_shop_by_id(cls,shop_id):
        return cls.objects.get(pk=shop_id)

class Package(models.Model):
    products = models.ManyToManyField(Product,blank=True,
)
    distributor = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True,blank=True)
    delivered = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    unique_together = ('products')

    @classmethod
    def add_to_package(cls, products, user):
        product_list =[(product) for product in products]
        package = cls.create_package(user)
        package.products.add(*product_list)
        return package
    
    @classmethod
    def create_package(cls, user):
        package = cls(delivered=True, distributor=user)
        package.save()
        return package
    
    @classmethod
    def remove_from_package(cls, package_id, product_id):
        product = Product.get_product_by_id(product_id)
        package = cls.get_package_by_id(package)
        package.products.remove(product)
        return package
        
    @classmethod
    def get_package_by_id(cls, package_id):
        package = cls.objects.get(package_id)
        return package


class Rating(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE,primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(null=False,blank=False)
    comment = models.TextField()
    
    unique_together = ('user')


    @classmethod
    def save_rating(cls,product_id,user_id,rating,comment):
        product = Product.get_product_by_id(product_id)
        user = User.objects.get(pk=user_id)
        rating = cls(user=user,product=product,rating=rating,comment=comment)
        rating.save()
        return rating

    @classmethod
    def get_products_rating(cls, product_id):
        results = cls.get_products_rating(product_id)
        ratings = []
        if results is not None:
            for rating in results:
                ratings.append(int(rating.rating))
        else:
            ratings.append(0)
        return ratings
   
    @classmethod
    def get_products_rating(cls, product_id):
        ratings = cls.objects.filter(product = product_id).all()
        return ratings

