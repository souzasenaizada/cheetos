from django.contrib import admin
from Salgadinho.models import Salgadinho, Brand

# Register your models here.
class SalgadinhoAdmin(admin.ModelAdmin):
    list_display = ('flavor', 'factory_day', 'value', 'taste', 'color')
    search_fields = ('flavor', 'factory_day', 'value', 'taste', 'color')
    
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand')
    search_fields = ('id', 'brand')


admin.site.register(Salgadinho, SalgadinhoAdmin)    #PARAMÊTROS PARA A PAGINA DE ADMIN
admin.site.register(Brand, BrandAdmin)