from django.contrib import admin
from .models import User, Farmer, Manufacturer,Distributor,ProductSet,Product,Rating,Shop, Package

# Register your models here.
admin.site.register(User)
admin.site.register(Farmer)
admin.site.register(Manufacturer)
admin.site.register(Distributor)
admin.site.register(ProductSet)
admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(Shop)
admin.site.register(Package)