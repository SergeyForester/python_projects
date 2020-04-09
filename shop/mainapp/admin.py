from django.contrib import admin

# Register your models here.
from mainapp.models import Product, Category, Species, Sort

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Species)
admin.site.register(Sort)