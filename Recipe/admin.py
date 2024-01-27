from django.contrib import admin
from .models import Product, Recipe, Ingredient


# Register your models here.
admin.site.register(Product)
admin.site.register(Recipe)
admin.site.register(Ingredient)
