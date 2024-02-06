from django.contrib import admin
from . import models 
@admin.register(models.Product)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('Product_name',)}
    list_display = ('Product_name','price','stock','Category','modified_date','is_available')
    
