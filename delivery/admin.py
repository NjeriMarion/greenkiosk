from django.contrib import admin
from .models import Delivery

# Register your models here.

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("Recipient_name", "Delivery_item", "no_of_products", "total_price", "delivery_address")
admin.site.register(Delivery, DeliveryAdmin)