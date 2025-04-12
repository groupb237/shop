from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    TYPE = (
        ('manager', 'manager'),
        ('customer', 'customer')
    )
    type = models.CharField(max_length=100, choices=TYPE, default="customer")
