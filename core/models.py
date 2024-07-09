from django.db import models

# Create your models here.
class clientes(models.Model): # creamos la base de datos con sus atributos
    rut = models.CharField(primary_key=True,max_length=12)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    Numero = models.CharField(max_length=50, null=True)

    def __str__(self): #el metodo __str__ es un metodo de python que nos permite mostrar que listar de la base de datos
        texto = "{0}"
        return texto.format(self.nombre)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self): #el metodo __str__ es un metodo de python que nos permite mostrar que listar de la base de datos
        texto = "{0}"
        return texto.format(self.nombre)
    
class Venta(models.Model):
    codigo_venta = models.CharField(primary_key=True, max_length=50)
    cliente = models.ForeignKey(clientes, on_delete=models.CASCADE, null=False)
    fecha_compra = models.DateField(null=False, blank=True)
    productos = models.ManyToManyField(Producto, through='DetalleVenta')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        texto = "{0}"
        return texto.format(self.codigo_venta)
    
class DetalleVenta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)




