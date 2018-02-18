from django.contrib import admin
from .models import ProductList
# Register your models here.
class ProductListAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_url', 'title')

admin.site.register(ProductList, ProductListAdmin)