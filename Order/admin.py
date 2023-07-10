from django.contrib import admin
from .models import Order

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "order_number", "order_date")
admin.site.register(Order, ProductAdmin)