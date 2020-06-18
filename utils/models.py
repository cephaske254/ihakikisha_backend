from django.db import models

class BaseAbstractModel(models.Model): 

    class Meta:
        abstract = True