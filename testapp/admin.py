from django.contrib import admin
from .models import Product
# Register your models here.
TEXT = "some thing wiill be typing"
class ProductAdmin(admin.ModelAdmin):
   # fields= ['name',('slug','is_digital',)]
    fieldsets = (
        ('part 1', {
           'fields':  ('name',), 
           'description': '%s' % TEXT,
        }),
        ('section 2', {
           'fields':  ('slug',),
           'classes':('collapse',)
        }),
        
        ('section 3',{
            'fields': ('is_digital',)
        }),
        
    )

admin.site.register(Product, ProductAdmin)