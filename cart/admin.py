from django.contrib import admin
from .models import Cart

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ("item_name", "item_price", "date_created")
admin.site.register(Cart, CartAdmin)
