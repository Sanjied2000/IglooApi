from django.contrib import admin
from .models import IceCream, Favourite, Order,Payment

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','orderdate') 
    filter_horizontal = ('icecream',) # Enables multi-select widget
    
@admin.register(IceCream)
class IceCreamAdmin(admin.ModelAdmin):
    list_display = ('id', 'icecreamName','price')  


admin.site.register(Favourite)
admin.site.register(Payment)