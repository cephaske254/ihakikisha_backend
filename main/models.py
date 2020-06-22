from django.db import models
from django.db.models import Q
from utils.models import BaseAbstractModel
import statistics
from authentication.models import User
from django.db.models import Q

class Manufacturer(BaseAbstractModel):
<<<<<<< HEAD
    name = models.CharField(max_length=255, null=False,blank=False,)
=======
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=255, null=False,blank=False)
>>>>>>> 270b9d347b1bd8a1868f8d2b420201e9495c08b9
    phone = models.IntegerField(blank=False, null=False)
    location = models.CharField(max_length=255, null=False,blank=False)
    email = models.EmailField(max_length=255)
    logo = models.ImageField(upload_to='profiles/manufacturer',default='avatar.png')

    def __str__(self):
        return 'Manufacturer - %s %s'%(self.name, self.email)
<<<<<<< HEAD
    
    @classmethod
    def add_manufacturer(cls, name, phone, location, email, logo):
        manufacturer = cls.objects.create(name=name, phone=phone, location=location, email=email, logo=logo)
        manufacturer.save()
        return manufacturer

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

=======
 

class Farmer(BaseAbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    image = models.ImageField(upload_to='profiles/farmer',default='avatar.png')
    
>>>>>>> 270b9d347b1bd8a1868f8d2b420201e9495c08b9

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
<<<<<<< HEAD
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
=======
        return '%s - (%s) | %s' %(self.product_set,self.pk, self.bought_not_bought)

>>>>>>> 270b9d347b1bd8a1868f8d2b420201e9495c08b9

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
   