from django.contrib import admin
from .models import Inventario
# Register your models here.
 
@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
	list_display=('pk','nombre','categoria','existencia')
	search_fields=('nombre',)
	list_filter = ('categoria',) 