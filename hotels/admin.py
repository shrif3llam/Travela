from django.contrib import admin

# Register your models here.

from .models import Hotel,Category

admin.site.register(Hotel)
admin.site.register(Category)