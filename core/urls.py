from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')), # esto carga todo lo relacionado con el login
    path('', views.home, name="home"),
    path('salir/', views.salir, name="salir"), # cerrar sesiòn
    path('historial_Compra', views.historial_Compra, name="historial_Compra"),
    path('menu_Historial', views.menu_Historial, name="menu_Historial"),
    path('registrar_Cliente', views.registrar_Cliente, name="registrar_Cliente"), # Vista registrar cliente
    path('registrarCliente', views.registrarCliente, name="registrarCliente"), # Función registrar cliente
    path('eliminarCliente/<rut>/', views.eliminardatosclientes, name="eliminarCliente"), # Eliminar cliente
    path('datosClientes/<rut>', views.editarcliente, name="datosClientes"), # Vista editar cliente
    path('editarVenta/<codigo_venta>', views.editarVenta, name="editarVenta"),
    path('guardarEdicion/', views.guardarEdicion, name="guardarEdicion"), # Función que almacena la edicion del cliente
    path('registrar_Cliente/', views.search_results, name="search_results"), # funcion de busqueda sacado de chatgpt
    path('guardarVenta/', views.prosesar_formulario_venta, name="guardarVenta"), # Funcion que almacena la venta
    path('regsitrar_Venta', views.regsitrar_Venta, name="regsitrar_Venta"),
    path('ultima_Compra/', views.ultima_Compra, name="ultima_Compra"),
    path('Alerta', views.Alerta, name="Alerta"),
    path('eliminarVenta/<codigo_venta>/', views.eliminarventa, name="eliminarVenta"),
    path('guardarventaedit/', views.guardarEdicionventa, name="guardarventaedit"),
    path('menu_Historial/', views.Filtrar_fecha, name="Filtrar_fecha"),
    path('Historial_compra/', views.historial_Compra, name="historialcompra"),
    path('registro/', views.registro, name='registro')

]
