from django.contrib import admin
from django.db import models
from .models import Product, Customer

# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)