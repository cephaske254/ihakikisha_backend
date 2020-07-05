from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from .models import User
# Register your models here.
admin.site.unregister(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields=['password']

TokenAdmin.raw_id_fields=['user']


