from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =['id','customer','date_order','complete','transaction_id']
    
admin.site.register(OrderItem)
admin.site.register(shippingAddress)    
     
     