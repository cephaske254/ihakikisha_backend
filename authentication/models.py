from django.db import models
from utils.models import BaseAbstractModel
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, AbstractUser

# Create your models here.

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,
                    email=None,
                    first_name=None,
                    last_name=None,
                    password=None,
                    role="AP"):
        if not first_name:
            raise ValueError('Firstname is required')

        if not last_name:
            raise ValueError('Lastname is required')

        if not email:
            raise ValueError('Email is required')

        if not password:
            raise ValueError('Password is required')

        if not role:
            raise ValueError('Role is required')

        user = self.model(
            email=self.normalize_email(email),
            username=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.role = role
        user.save()
        return user

    def create_superuser(
            self, first_name=None, last_name=None, email=None, password=None):
        """Create a `User` who is also a superuser"""
        if not first_name:
            raise TypeError('Superusers must have a first name.')

        if not last_name:
            raise TypeError('Superusers must have a last name.')

        if not email:
            raise TypeError('Superusers must have an email address.')

        if not password:
            raise TypeError('Superusers must have a password.')

        user = self.model(
            first_name=first_name, last_name=last_name,
            email=self.normalize_email(email), role='LA')
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.is_verified = True
        user.set_password(password)
        user.save()

class User(AbstractUser, BaseAbstractModel):
    USER_TYPE_CHOICES =(
        ('A', 'admin'),
        ('M','manufacturer'),
        ('F','farmer'),
        ('D','distributor'),
    )
    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=20)
    objects = UserManager()