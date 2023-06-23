from django.contrib import admin
from .models import Sign_up

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
admin.site.register(Sign_up, CustomerAdmin)
