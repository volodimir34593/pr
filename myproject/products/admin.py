from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    # Додайте інші налаштування адміністратора за потребою

admin.site.register(Product, ProductAdmin)

# Register your models here.
