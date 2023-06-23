from django.db import models

# Create your models here.
class Delivery(models.Model):
    Recipient_name=models.CharField(max_length=32)
    total_price=models.DecimalField(max_digits=8,decimal_places=2)
    Delivery_item=models.TextField()
    image=models.ImageField()
    date_requested=models.DateTimeField(auto_now_add=True)
    no_of_products=models.PositiveIntegerField()
    delivery_address= models.CharField(max_length=40)