from django.contrib import admin

from .models import Order, Customer, Product

class adminCustomer(admin.ModelAdmin):
    search_fields = ('company','last_name','first_name', 'phone')
    list_display = ('company','first_name','last_name','updated_at', 'created_at')

class adminProduct(admin.ModelAdmin):
    search_fields = ('code','desc')
    list_display = ('code', 'desc', 'price')

class adminOrder(admin.ModelAdmin):
    search_fields = ('code',)
    list_display = ('code','updated_at', 'created_at', 'status')
    list_filter = ('status','updated_at','created_at')

admin.site.register(Customer, adminCustomer)
admin.site.register(Product, adminProduct)
admin.site.register(Order, adminOrder)

