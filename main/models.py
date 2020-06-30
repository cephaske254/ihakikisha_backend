from django.db import models
from utils.models import BaseAbstractModel

from authentication.models import User
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, pre_save

import qrcode
from django.conf import settings
import os

from .validators import validate_phone, validate_manufactured

import cloudinary
from cloudinary.models import CloudinaryField


class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True,editable=False)

    class Meta:
        abstract = True


class Manufacturer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    name = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(blank=False, null=False,
                             max_length=13, validators=[validate_phone])
    location = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255)
    logo = CloudinaryField(default='avatar.png')

    def __str__(self):
        return 'Manufacturer - %s %s' % (self.name, self.email)


class Farmer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,related_name='profile_m')
    image = CloudinaryField(default='avatar.png')


class Distributor(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, blank=True)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name='profile', blank=True)
    

    def __str__(self):
        return 'Distributor - %s %s' % (self.user.first_name, self.manufacturer)

    class Meta:
        unique_together = (('user', 'manufacturer'))


class ProductSet(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False, blank=False)
    composition = models.TextField(null=False, blank=False)
    image = CloudinaryField(null=False, blank=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s by %s' % (self.name, self.manufacturer.name)

    class Meta:
        unique_together=('name',)


class Product(BaseModel):
    product_set = models.ForeignKey(ProductSet, on_delete=models.CASCADE, related_name='products')
    qr_code = CloudinaryField(blank=True)
    sold = models.BooleanField(default=False)
    manufactured = models.DateField(auto_now_add=False, auto_now=False,validators=[validate_manufactured])
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - (%s)' % (self.product_set, self.pk)

    def save(self, *args, **kwargs):
        if not self.qr_code:
            self.qr_code = f'{self.uuid}.png'
            super(Product, self).save(*args, **kwargs)

    def delete(self):
        upload_to = f'{self.uuid}.png'
        image_name = f'{settings.MEDIA_ROOT}/{upload_to}'
        if os.path.isfile(image_name):
            os.remove(image_name)
            cloudinary.uploader.destroy(self.uuid)
        super(Product, self).delete()


class Shop(BaseModel):
    name = models.CharField(max_length=255, null=False,
                            blank=False, unique=True)
    phone = models.IntegerField(blank=False, null=False, unique=True)
    location = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = (('name', 'phone', 'location'), ('name', 'location'))


class Package(BaseModel):
    products = models.ManyToManyField(Product, blank=True,)
    distributor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, null=True, blank=True)
    delivered = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    unique_together = ('products')


class Rating(models.Model):
    product_set = models.ForeignKey(
        ProductSet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False)
    rating = models.PositiveIntegerField(null=False, blank=False)
    comment = models.TextField(null=True, blank=True)

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


@receiver(post_save, sender=Product)
def generate_qr(sender, instance, **kwargs):
    upload_to = f'qr_codes/{instance.uuid}.png'

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_M,
        box_size=10,
        border=3
    )

    data = instance.uuid
    qr.add_data(data)
    qr.make(fit=True)
    cloudinary.uploader.destroy(str(instance.uuid))
    img = qr.make_image(fill='black', back_color='white')
    image_name = f'{settings.MEDIA_ROOT}/{upload_to}'

    img.save(image_name)

    cloudinary_image = cloudinary.uploader.upload_image(
        image_name,
        public_id=str(instance.uuid),
        overwrite=True,
    )

    image_url = cloudinary_image
