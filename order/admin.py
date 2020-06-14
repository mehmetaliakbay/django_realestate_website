from django.contrib import admin
from order.models import ShopCart

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['user','myproperty','price','address']
    list_filter = ['user']

admin.site.register(ShopCart, ShopCartAdmin)