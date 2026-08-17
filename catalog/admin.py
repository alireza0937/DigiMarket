from django.contrib import admin
from .models import Category, Product, ProductImage, SellerProfile, Tag

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(SellerProfile)
admin.site.register(Tag)