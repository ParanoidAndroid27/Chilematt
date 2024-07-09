from django.contrib import admin
from.models import clientes, Venta, DetalleVenta, Producto
# Register your models here.

admin.site.register(clientes)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Producto)
