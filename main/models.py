from django.db import models
from utils.models import BaseAbstractModel
import statistics
from authentication.models import User
from django.db.models import Q

class Manufacturer(BaseAbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=255, null=False,blank=False)
    phone = models.IntegerField(blank=False, null=False)
    location = models.CharField(max_length=255, null=False,blank=False)
    email = models.EmailField(max_length=255)
    logo = models.ImageField(upload_to='profiles/manufacturer',default='avatar.png')

    def __str__(self):
        return 'Manufacturer - %s %s'%(self.name, self.email)
 

class Farmer(BaseAbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    image = models.ImageField(upload_to='profiles/farmer',default='avatar.png')
    

class Distributor(BaseAbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    manufacturer = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer')
    

class ProductSet(models.Model):
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False,blank=False)
    composition = models.TextField(null=False,blank=False)
    qr_code = models.CharField(max_length=500)
    image = models.ImageField(upload_to='products',null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s by %s'%(self.name,self.manufacturer.name)


class Product(models.Model):
    product_set = models.ForeignKey(ProductSet,on_delete=models.CASCADE)
    qr_code = models.CharField(max_length=500)
    sold = models.BooleanField(default=False)
    manufactured = models.DateField(auto_now_add=False, auto_now=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - (%s) | %s' %(self.product_set,self.pk, self.bought_not_bought)


class Shop(models.Model):
    name = models.CharField(max_length=255, null=False,blank=False, unique=True)
    phone = models.IntegerField(blank=False, null=False, unique=True)
    location = models.CharField(max_length=255, null=False,blank=False)
    email = models.EmailField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        unique_together=(('name','phone','location'),('name','location'))
    
class Package(models.Model):
    products = models.ManyToManyField(Product,blank=True,
)
    distributor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True,blank=True)
    delivered = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    unique_together = ('products')


class Rating(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE,primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(null=False,blank=False)
    comment = models.TextField()

    unique_together = 'user'

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
   