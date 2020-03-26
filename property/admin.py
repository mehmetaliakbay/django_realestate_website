from django.contrib import admin
from property.models import Category, Property, Images


# Register your models here.


class PropertyImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)



class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price_rent',
                    'price_sell',  'image_tag', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status', 'category']
    inlines = [PropertyImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'property', 'image_tag']
    readonly_fields = ('image_tag',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Images, ImagesAdmin)
