from django.contrib import admin
from .models import CategoriaProducto, Producto

# Register your models here.

class CategoriaProductosAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated") #Indicamos que estos dos datos son de solo lectura

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated") #Idem anterior

#Aqui registramos las tablas de los modelos Prod, CatProd y las clases de arriba
admin.site.register(CategoriaProducto,CategoriaProductosAdmin)
admin.site.register(Producto, ProductoAdmin)

