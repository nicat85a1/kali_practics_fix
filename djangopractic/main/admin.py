from django.contrib import admin
from main.models import Car
from .models import Car
from main.models import *
# Register your models here.

admin.site.register(Car)