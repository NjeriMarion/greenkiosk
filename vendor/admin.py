from django.contrib import admin
from .models import Vendor

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name",)
admin.site.register(Vendor, ProductAdmin)