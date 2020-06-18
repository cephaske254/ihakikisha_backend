from django.db import models
from utils.models import BaseAbstractModel
import statistics
from authentication.models import User


class Farmer(BaseAbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    image = models.ImageField(upload_to='profiles/farmer',default='avatar.png')


class Manufacturer(BaseAbstractModel):
    name = models.CharField(max_length=255, null=False,blank=False)
    phone = models.IntegerField(blank=False, null=False)
    location = models.CharField(max_length=255, null=False,blank=False)
    email = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='profiles/manufacturer',default='avatar.png')

    def __str__(self):
        return 'Manufacturer - %s %s'%(self.name, self.email)

class Distributor(BaseAbstractModel):
    manufacturer = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer')
    image = models.ImageField(upload_to='profiles/distributor',default='avatar.png')
    


class ProductSet(models.Model):
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False,blank=False)
    composition = models.TextField(null=False,blank=False)
    image = models.ImageField(upload_to='',null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s by %s'%(self.name,self.manufacturer.user.profile.name)

class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    manufactured = models.DateField()
    product_set = models.ForeignKey(ProductSet,on_delete=models.CASCADE)
    qr_code = models.CharField(max_length=500)
    sold = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    @property
    def average_rating(self):
        product_id = self.id
        raw_ratings = Rating.get_products_rating(self.id)
        rating = round(statistics.mean(raw_ratings),1)
        return rating

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

class Shop(models.Model):
    name = models.CharField(max_length=255, null=False,blank=False)
    phone = models.IntegerField(blank=False, null=False)
    location = models.CharField(max_length=255, null=False,blank=False)
    email = models.CharField(max_length=255)
