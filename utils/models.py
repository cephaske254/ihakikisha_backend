from django.db import models
from django.contrib.auth.models import BaseUserManager
import uuid

class BaseAbstractModel(models.Model): 
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    class Meta:
        abstract = True

class UserManager(BaseUserManager):
    def create_user(self,first_name,last_name,email, password, user_type='F'):
        if not email:
             raise ValueError("Email is required")
        if not first_name:
            raise ValueError("First Name is required")
        if not last_name:
            raise ValueError("Last Name is required")
        if not password:
            raise ValueError("Password is required")
        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            user_type = user_type,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,first_name,last_name,email, password, user_type='A'):
        if not email:
            raise ValueError("Email is required")
        if not first_name:
            raise ValueError("First Name is required")
        if not last_name:
            raise ValueError("Last Name is required")
        if not password:
            raise ValueError("Password is required")
        user = self.create_user(first_name,last_name,email,password,user_type='A')
        user.staff = True
        user.admin = True
        user.superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user