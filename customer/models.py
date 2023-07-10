from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete =models.CASCADE)
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=16)
    password_confirmation = models.CharField(max_length=16)
