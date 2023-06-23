from django.db import models

# Create your models here.
class Sign_up(models.Model):
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=16)
    password_confirmation = models.CharField(max_length=16)
