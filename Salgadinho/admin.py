from django.contrib import admin
from Salgadinho.models import Salgadinho

# Register your models here.
class SalgadinhoAdmin(admin.ModelAdmin):
    list_display = ('flavor', 'factory_day', 'value', 'taste', 'color')
    search_fields = ('flavor', 'factory_day', 'value', 'taste', 'color')

admin.site.register(Salgadinho, SalgadinhoAdmin)    #PARAMÊTROS PARA A PAGINA DE ADMIN
