from django.contrib import admin
from .models import User, Farmer, Manufacturer, Distributor, ProductSet, Product, Rating, Shop, Package
from django import forms
from cloudinary.forms import CloudinaryInput
# Register your models here.


# class ProductAdmin(admin.ModelAdmin):
#     readonly_fields = ('qr_code', )


admin.site.register(User)
admin.site.register(Farmer)
admin.site.register(Manufacturer)
admin.site.register(Distributor)
admin.site.register(ProductSet)
admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(Shop)
admin.site.register(Package)
