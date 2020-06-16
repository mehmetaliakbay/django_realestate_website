from django.contrib import admin

from order.models import ShopCart, OrderProperty, Order


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['user','myproperty','price','address']
    list_filter = ['user']

class OrderPropertyline(admin.TabularInline):
    model = OrderProperty
    readonly_fields = ('user', 'property', 'price', 'quantity', 'amount')
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'total', 'status']
    list_filter = ['status']
    readonly_fields = (
        'user',  'phone', 'first_name', 'ip', 'last_name', 'phone', 'total')
    inlines = [OrderPropertyline]


class OrderPropertyAdmin(admin.ModelAdmin):
    list_display = ['user', 'property', 'price', 'quantity', 'amount']
    list_filter = ['user']


admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProperty, OrderPropertyAdmin)