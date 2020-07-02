from django.db import models
from utils.models import BaseAbstractModel
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from utils.models import UserManager, BaseAbstractModel

from django.db.models.signals import post_save,post_delete, pre_save
from django.dispatch import receiver
# Create your models here.


class User(BaseAbstractModel, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=120, null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False,null=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    superuser = models.BooleanField(default=False) # a superuser
    date_joined = models.DateField(auto_now_add=True) # a superuser
    USER_TYPE_CHOICES =(
        ('A', 'admin'),
        ('M','manufacturer'),
        ('F','farmer'),
        ('D','distributor'),
    )
    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=20, null=False, blank=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type', 'first_name', 'last_name']
    objects = UserManager()

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    @property
    def is_superuser(self):
        "Is the user active?"
        return self.superuser


    @classmethod
    def add_user(cls, first_name, last_name, email, password, user_type):
        user = cls.objects.create_user(first_name,last_name,email,password,user_type=user_type)
        return user

    @classmethod
    def edit_user(cls,user_id, first_name, last_name, email):
        user = cls.get_user_by_id(user_id)
        if user:
            user.first_name = first_name or user.first_name
            user.last_name = first_name or user.last_name
            user.email = email or user.email
            user.save()
            return user
        return None
    
    @classmethod
    def get_user_by_id(cls, user_id):
        try:
            user = cls.objects.get(pk=user_id)
            return user
        except:
            return None

    def save(self, *args, **kwargs):
        if self.admin == False or self.superuser == False:
            self.set_password(self.password)
        super(User, self).save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    from main.models import  Manufacturer, Farmer, Distributor

    if instance.user_type == 'F':
        profile = Farmer.objects.update_or_create(user = instance)

    elif instance.user_type == 'M':
        profile = Manufacturer.objects.update_or_create(user = instance, phone=0, email=instance.email)
