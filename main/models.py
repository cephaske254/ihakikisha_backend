from django.db import models
from utils.models import BaseAbstractModel
import statistics
from authentication.models import User


class Farmer(BaseAbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    image = models.ImageField(upload_to='profiles/farmer',default='avatar.png')
    
    @classmethod
    def update_farmer(cls, user, image):
        profile = cls.objects.create(user=user, image=image).save()
        return profile


class Manufacturer(BaseAbstractModel):
    name = models.CharField(max_length=255, null=False,blank=False related_name='profile')
    phone = models.IntegerField(blank=False, null=False)
    location = models.CharField(max_length=255, null=False,blank=False)
    email = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='profiles/manufacturer',default='avatar.png')

    def __str__(self):
        return 'Manufacturer - %s %s'%(self.name, self.email)
    
    @classmethod
    def add_manufacturer(cls, name, phone, location, email, logo):
        manufacturer = cls.objects.create(name=name, phone=phone, location=location, email=email, logo=logo)
        manufacturer.save()
        return manufacturer
        
    @classmethod
    def search_product(cls,query):
        products= cls.object.filter(Q(product_product=query)).all()
        return products

    @classmethod
    def update_product(cls,id, name, manufactured, qr_code, sold, date):
        product = cls.get_product_by_id(id)
        product.name = name or product.name
        product.manufactured = manufactured or product.manufactured
        product.qr_code = qr_code or product.qr_code
        product.sold = sold or product.sold
        product.date = date or product.date
        product.save()
        return product

    @classmethod
    def get_product_by_id(cls, id):
        return cls.objects.get(pk=id)

    @receiver(post_save, sender=User)
    def create_manufacturer_profile(sender, instance, created, **kwargs):
        if created:
            Manufacturer.ojects.create(name=instance)
    
    @receiver(post_save, sender=User)
    def save_manufacturer_profile(sender, instance, **kwargs):
       instance.profile.save()

    def __str__(self):
        return self.username.username

    @classmethod
    def search_product(cls,search_term):
        product_name = cls.object.filter(Q(product_product=search_term))
        return product_name

    @classmethod
    def save_distributor(cls,user,manufacturer,image):
        distributor = cls(user=user,manufacturer=manufacturer,image=image)
        distributor.save()
        return distributor

    @classmethod
    def update_product(cls,id, name, manufactured, qr_code, sold, date):
        product = cls.get_product_by_id(id)
        product.name = name or product.name
        product.manufactured = manufactured or product.manufactured
        product.qr_code = qr_code or product.qr_code
        product.sold = sold or product.sold
        product.date = date or product.date
        product.save()
        return product

    @classmethod
    def delete_productset(cls,ProductSet):
        cls.objects.filter(ProductSet=ProductSet).delete()


class Distributor(BaseAbstractModel):
    manufacturer = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer')
    image = models.ImageField(upload_to='profiles/distributor',default='avatar.png')
    

    @classmethod
    def save_distributor(cls,user,manufacturer,image):
        distributor = cls(user=user,manufacturer=manufacturer,image=image)
        distributor.save()
        return distributor


    @classmethod
    def get_distributor(cls,user):
        distributor = cls.objects.filter(id=user.id).first()
        return distributor

    @classmethod
    def update_distributor_info(cls,user,manufacturer,image):
        distributor = cls.get_distributor(user)
        distributor.manufacturer = manufacturer or distributor.manufacturer
        distributor.image = image or distributor.image
        distributor.save()
        return distributor

    @classmethod
    def get_manufacturer_distributor(cls,manufacturer):
        distributors = cls.objects.filter(manufacturer=manufacturer.id).all()
        return distributors

    @classmethod
    def remove_distributor(cls,user):
        distributor = cls.objects.get(user=user)
        distributor.delete()

class ProductSet(models.Model):
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False,blank=False)
    composition = models.TextField(null=False,blank=False)
    qr_code = models.CharField(max_length=500)
    image = models.ImageField(upload_to='products',null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s by %s'%(self.name,self.manufacturer.user.profile.name)

    
    def __str__(self):
        return '%s by %s'%(self.name,self.manufacturer.user.profile.name)

    @classmethod
    def create_product_set(cls,name,manufactured,product_set,qr_code,sold,date):
        product = cls(name=name,manufacured=manufacured,product_set=product_set,qr_code=qr_code,sold=sold,date=date)
        product.save()
        return product

    @classmethod
    def update_product_set(cls,id, name, description, composition, image):
        product_set = cls.get_product_set_by_id(id)
        product_set.name = name or product_set.name
        product_set.composition = composition or product_set.composition
        product_set.description = sold or product_set.description
        product_set.image = date or product_set.image
        product.save()
        return product_set

    @classmethod
    def delete_product_set(cls,id):
        product_set = cls.get_product_set_by_id(id)
        product_set.delete()

    @classmethod
    def get_all(cls):
        product_sets = cls.objects.all()
        return product_sets

    @classmethod
    def get_product_set_by_id(cls,id):
        product_set = cls.objects.get(pk=id)
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

    @classmethod
    def create_product(cls,name,manufactured,product_set,qr_code,sold,date):
        product = cls(name=name,manufacured=manufacured,product_set=product_set,qr_code=qr_code,sold=sold,date=date)
        product.save()
        return product
    
    @classmethod
    def create_product(cls,name,manufactured,product_set,qr_code,sold,date):
        product = cls(name=name,manufacured=manufacured,product_set=product_set,qr_code=qr_code,sold=sold,date=date)
        product.save()
        return product

    @classmethod
    def update_product(cls,id, name, manufactured, qr_code, sold):
        product = cls.get_product_by_id(id)
        product.name = name or product.name
        product.manufactured = manufactured or product.manufactured
        product.qr_code = qr_code or product.qr_code
        product.sold = sold or product.sold
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
    def update_product(cls,id, name, manufactured, qr_code, sold, date):
        product = cls.get_product_by_id(id)
        product.name = name or product.name
        product.manufactured = manufactured or product.manufactured
        product.qr_code = qr_code or product.qr_code
        product.sold = sold or product.sold
        product.date = date or product.date
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


class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    manufactured = models.DateField()
    product_set = models.ForeignKey(ProductSet,on_delete=models.CASCADE)
    qr_code = models.CharField(max_length=500)
    sold = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def search_product(cls,search_term):
        product = cls.object.filter(Q(product.name=search_term))
        return product

    @property
    def average_rating(self):
        product_id = self.id
        raw_ratings = Rating.get_products_rating(self.id)
        rating = round(statistics.mean(raw_ratings),1)
        return rating


class Shop(models.Model):
    name = models.CharField(max_length=255, null=False,blank=False)
    phone = models.IntegerField(blank=False, null=False)
    location = models.CharField(max_length=255, null=False,blank=False)
    email = models.CharField(max_length=255)


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


class Rating(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE,primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(null=False,blank=False)
    comment = models.TextField()

    @classmethod
    def get_products_rating(cls, product_id):
        results = cls.objects.filter(product = product_id).all()  
        ratings = []
        if results is not None:
            for rating in results:
                ratings.append(int(rating.rating))
        else:
            ratings.append(0)
        return ratings
