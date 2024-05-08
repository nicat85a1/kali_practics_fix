from django.contrib import admin
from .models import Product, UserProfile, Tag

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","explanation"]

admin.site.register(UserProfile)

admin.site.register(Tag)