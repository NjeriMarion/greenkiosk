from django.db import models
from inventory.models import Product

# Create your models here.
class Cart(models.Model):
    products = models.ManyToManyField(Product)
    item_name=models.CharField(max_length=32)
    item_price=models.DecimalField(max_digits=8,decimal_places=2)
    date_created=models.DateTimeField(auto_now_add=True)
    # no_of_items = models.IntegerField()
    total = models.IntegerField
    # totals = item_price * no_of_items