from django.contrib import admin
from .models import *
mymodel=[Product,Customer,Order,Inventory]
# Register your models here.
for model in mymodel:
    admin.site.register(model)
