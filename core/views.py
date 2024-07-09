from django.shortcuts import render, HttpResponse, redirect
from .models import clientes, Venta, Producto, DetalleVenta
from django.contrib.auth.decorators import login_required # el login required, oculta las vistas y solo permite iniciar luego del login 
from django.contrib.auth import logout # para el cerrar sesión
from datetime import date
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from .forms import VentaForm, DetalleVentaFormSet
from django.contrib.auth import login, authenticate
from .forms import RegistroForm

@login_required
def home(request): #Funcion la cual se encarga de obtener datos la ultimas compras realizada por los clientes
    icono_count = 0
    lista_venta = [] #Lista la cual es la úlitma compra de cada Cliente
    productos = Producto.objects.all()
    Clientes = clientes.objects.all() #Llama a todos los clientes que se encuentra en models
    #Esta lista se utiliza para la funcion en la cual te trae la ultima fecha de venta registrada del cliente
    Clientes_list = clientes.objects.all() #Esto es para cargar los datos de los clientes a la venta 
    today = date.today()
    message = [] #Variable que almacena los mensajes de atraso de un cliente
    #Ej "Han pasado",delta.days ," Días desde que el cliente", Clientes.nombre,"no a realizado una compra")) 
    #Este for itera por cada cliente
    for Clientes in Clientes:
        if Venta.objects.filter(cliente = Clientes).order_by('-fecha_compra').first() is None:
            print("Cliente no posee Compras")
        else:
            ultima_fecha = Venta.objects.filter(cliente = Clientes).order_by('-fecha_compra').first()
            lista_venta.append(ultima_fecha)#Append inserta un dato en un arreglo, esto inserta la ultima compra realizada por el cliente
            fecha_rgistrada = ultima_fecha.fecha_compra #Almacena solo la ultima fecha del cliente que se este recorriendo
            delta = today - fecha_rgistrada
            if delta.days >= 14:
                message.append(("Han pasado",delta.days ," Días desde que el cliente", Clientes.nombre,"no a realizado una compra"))
                icono_count = icono_count + 1 
            else:
                print("No han pasado 2 semanas") 
    lista_venta = sorted(lista_venta, key=lambda lista_venta: lista_venta.fecha_compra) #Esto lo puse para ordenarlo
    detalles_ventas = []
    for venta in lista_venta:
        detalles_venta = []
        detalles = DetalleVenta.objects.filter(venta=venta)
        for detalle in detalles:
            producto = detalle.producto
            detalles_venta.append({
                'producto': producto.nombre,
                'precio': producto.precio,
                'cantidad': detalle.cantidad
                
            })
        detalles_ventas.append({
            'venta': venta,
            'detalles': detalles_venta
        })
        """ detalles_ventas.sort(Venta.objects.order_by('-fecha_compra')) """
    return render(request, 'core/home.html', {"venta_list": detalles_ventas ,"clientes_lista": Clientes_list,'message': message,  "contador": icono_count, 'productos': productos})

@login_required
def salir(request): # cerrar sesion
    logout(request)
    return redirect('/')

@login_required#Eliminar en futuro
def historial_Compra(request):
    icono_count = 0 # estro es para cargar el contador que esta en la alerta
    Clientes = clientes.objects.all() # estro es para cargar el contador que esta en la alerta
    today = date.today() # estro es para cargar el contador que esta en la alerta
    for Clientes in Clientes: # estro es para cargar el contador que esta en la alerta
        if Venta.objects.filter(cliente = Clientes).order_by('-fecha_compra').first() is None:
            print("Cliente no posee Compras")
        else:
            ultima_fecha = Venta.objects.filter(cliente = Clientes).order_by('-fecha_compra').first()
            fecha_rgistrada = ultima_fecha.fecha_compra #Almacena solo la ultima fecha del cliente que se este recorriendo
            delta = today - fecha_rgistrada
            if delta.days >= 14:
                icono_count = icono_count + 1 
            else:
                icono_count = icono_count + 0
    return render(request,'core/regsitrar_Venta.html',{"contador": icono_count})

@login_required
def menu_Historial(request):#Carga el historial general de las ventas
    venta_historial = Venta.objects.all()
    productos = Producto.objects.all()
    ventas = Venta.objects.order_by('-fecha_compra').all()
    Clientes_list = clientes.objects.all() # esto es para cargar los datos de los clientes a la venta 
    detalles_ventas = []
    for venta in ventas:
        detalles_venta = []
        detalles = DetalleVenta.objects.filter(venta=venta)
        for detalle in detalles:
            producto = detalle.producto
            detalles_venta.append({
                'producto': producto.nombre,
                'precio': producto.precio,
                'cantidad': detalle.cantidad
                
            })
        detalles_ventas.append({
            'venta': venta,
            'detalles': detalles_venta
        })
        
    icono_count = 0 # estro es para cargar el contador que esta en la alerta
    Clientes = clientes.objects.all() # estro es para cargar el contador que esta en la alerta
    today = date.today() # estro es para cargar el contador que esta en la alerta
    for Clientes in Clientes: # estro es para cargar el contador que esta en la alerta
        if Venta.objects.filter(cliente = Clientes).order_by('-fecha_compra').first() is None:
            print("Cliente no posee Compras")
        else:
            ultima_fecha = Venta.objects.filter(cliente = Clientes).order_by('-fecha_compra').first()
            fecha_rgistrada = ultima_fecha.fecha_compra #Almacena solo la ultima fecha del cliente que se este recorriendo
            delta = today - fecha_rgistrada
            if delta.days >= 14:
                icono_count = icono_count + 1 
            else:
                icono_count = icono_count + 0
    return render(request, 'core/menu_Historial.html', {'productos': productos, "clientes_lista": Clientes_list, "venta_historial": detalles_ventas, "contador": icono_count})

@login_required
def registrar_Cliente(request):
    Clientes_lists = clientes.objects.all() # esto es para listar mediante orm
    Clientes_list = clientes.objects.all() # esto es para cargar los datos de los clientes a la venta
    productos = Producto.objects.all()

    icono_count = 0 # estro es para cargar el contador que esta en la alerta
    Clientes = clientes.objects.all() # estro es para cargar el contador que esta en la alerta
    today = date.today() # estro es para cargar el contador que esta en la alerta
    for Clientes in Clientes: # estro es para cargar el contador que esta en la alerta
        if Venta.objects.filter(cliente = Clientes).order_by('-fecha_compra').first() is None:
            print("Cliente no posee Compras")
        else:
            ultima_fecha = Venta.objects.filter(cliente = Clientes).order_by('-fecha_compra').first()
            fecha_rgistrada = ultima_fecha.fecha_compra #Almacena solo la ultima fecha del cliente que se este recorriendo
            delta = today - fecha_rgistrada
            if delta.days >= 14:
                icono_count = icono_count + 1 
            else:
                icono_count = icono_count + 0
    return render(request, 'core/registrar_Cliente.html', {'productos': productos, "clientes_list": Clientes_lists, "clientes_lista": Clientes_list,"contador": icono_count})

@login_required
def registrarCliente(request):
    rut = request.POST['txtRut']
    nombre = request.POST['txtNombre']
    direccion = request.POST['txtDireccion']
    email = request.POST['txtEmail']
    numero = request.POST['txtNumero']

    try: #Obtiene los clientes registrados y los compara con el rut ingresado si este es igual no lo almacena.
        cliente = clientes.objects.get(rut=rut)
    except ObjectDoesNotExist:
        # Si no existe el cliente, lo crea.
        clientes.objects.create(rut=rut, nombre=nombre, direccion=direccion, email=email, Numero=numero)

    return redirect("/registrar_Cliente")

@login_required
def eliminardatosclientes(request, rut): # Eliminar cliente
    Cliente = clientes.objects.get(rut=rut)  #valida el rut y obtiene los datos 
    Cliente.delete() #se encarga de borrarlos
    return redirect('/registrar_Cliente')

@login_required
def editarcliente(request, rut): # redirecciona enviando el rut a la ventana cliente
    cliente = clientes.objects.get(rut=rut)
    Clientes_list = clientes.objects.all() # esto es para cargar los datos de los clientes a la venta

    icono_count = 0 # estro es para cargar el contador que esta en la alerta
    Clientes = clientes.objects.all() # estro es para cargar el contador que esta en la alerta
    today = date.today() # estro es para cargar el contador que esta en la alerta
    for Clientes in Clientes: # estro es para cargar el contador que esta en la alerta
        if Venta.objects.filter(cliente = Clientes).order_by('-fecha_compra').first() is None:
            print("Cliente no posee Compras")
        else:
            ultima_fecha = Venta.objects.filter(cliente = Clientes).order_by('-fecha_compra').first()
            fecha_rgistrada = ultima_fecha.fecha_compra #Almacena solo la ultima fecha del cliente que se este recorriendo
            delta = today - fecha_rgistrada
            if delta.days >= 14:
                icono_count = icono_count + 1 
            else:
                icono_count = icono_count + 0
    return render(request, "core/editar_Cliente.html", {'client':cliente, "clientes_lista": Clientes_list, "contador": icono_count}) 

@login_required
def editarVenta(request, codigo_venta): # redirecciona enviando el rut a la ventana cliente
    venta = get_object_or_404(Venta, pk=codigo_venta)
    
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        formset = DetalleVentaFormSet(request.POST, instance=venta)
        print(form.errors)
        print(formset.errors)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            print("hola")
            return redirect('/menu_Historial')
    else:
        form = VentaForm(instance=venta)
        formset = DetalleVentaFormSet(instance=venta)
    Clientes_list = clientes.objects.all() # esto es para cargar los datos de los clientes a la venta
    productos = Producto.objects.all()

    icono_count = 0 # estro es para cargar el contador que esta en la alerta
    Clientes = clientes.objects.all() # estro es para cargar el contador que esta en la alerta
    today = date.today() # estro es para cargar el contador que esta en la alerta
    for Clientes in Clientes: # estro es para cargar el contador que esta en la alerta
        if Venta.objects.filter(cliente = Clientes).order_by('-fecha_compra').first() is None:
            print("Cliente no posee Compras")
        else:
            ultima_fecha = Venta.objects.filter(cliente = Clientes).order_by('-fecha_compra').first()
            fecha_rgistrada = ultima_fecha.fecha_compra #Almacena solo la ultima fecha del cliente que se este recorriendo
            delta = today - fecha_rgistrada
            if delta.days >= 14:
                icono_count = icono_count + 1 
            else:
                icono_count = icono_count + 0
    return render(request, "core/editar_Venta.html", {'productos': productos, "clientes_lista": Clientes_list, "contador": icono_count, 'form': form, 'formset': formset}) 
    
@login_required
def guardarEdicionventa(request): # Guardar los datos del cliente
    codigo_venta = request.POST['txtCodigo'] #obtiene los datos de los labels
    cliente_nombre = request.POST['txtCliente']
    cliente = clientes.objects.get(nombre = cliente_nombre)
    fecha_compra = request.POST['datefecha']

    venta = Venta.objects.get(codigo_venta=codigo_venta)
    venta.codigo_venta = codigo_venta
    venta.cliente = cliente
    venta.fecha_compra = fecha_compra
    venta.save() #se encarga de crear guardar los datos obtenidos
        # Recorrer los datos del formulario para obtener los productos y sus cantidades
    for key, value in request.POST.items():
        if key.startswith('producto'):
            # Obtener el ID del producto a partir del nombre del campo
            producto_id = int(value)
            producto = Producto.objects.get(pk=producto_id)

            # Obtener la cantidad del producto a partir del nombre del campo
            cantidad_key = key.replace('producto', 'cantidad')
            cantidad = int(request.POST[cantidad_key])

            # Crear nuevo detalle de venta
            detalle_venta = DetalleVenta()
            detalle_venta.venta = venta
            detalle_venta.producto = producto
            detalle_venta.cantidad = cantidad
            detalle_venta.precio_unitario = producto.precio
            detalle_venta.subtotal = detalle_venta.precio_unitario * detalle_venta.cantidad
            detalle_venta.save()

            # Actualizar el total de la venta
            venta.total += detalle_venta.subtotal

    # Guardar la venta con el total actualizado
    venta.save()

    return redirect('/menu_Historial')


@login_required
def guardarEdicion(request): # Guardar los datos del cliente
    rut = request.POST['txtRut']
    nombre = request.POST['txtNombre']
    direccion = request.POST['txtDireccion']
    email = request.POST['txtEmail']
    numero = request.POST['txtNumero']

    cliente = clientes.objects.get(rut=rut)
    cliente.nombre = nombre
    cliente.direccion = direccion
    cliente.email = email
    cliente.Numero = numero
    cliente.save()

    return redirect('/registrar_Cliente')

@login_required
def prosesar_formulario_venta(request):
    if request.method == 'POST':
        codigo_venta = request.POST['txtCodigo'] #obtiene los datos de los labels
        cliente_nombre = request.POST['txtCliente']
        cliente = clientes.objects.get(nombre = cliente_nombre)
        fecha_compra = request.POST['datefecha']
        # Crear nueva venta
        venta = Venta()
        venta.codigo_venta = codigo_venta
        venta.cliente = cliente
        venta.fecha_compra = fecha_compra
        try:
            ventas = Venta.objects.get(codigo_venta=codigo_venta)
            return redirect('realizar_venta')
        except ObjectDoesNotExist:
            venta.save() #se encarga de crear guardar los datos obtenidos

        

            # Recorrer los datos del formulario para obtener los productos y sus cantidades
            for key, value in request.POST.items():
                if key.startswith('producto'):
                    # Obtener el ID del producto a partir del nombre del campo
                    producto_id = int(value)
                    producto = Producto.objects.get(pk=producto_id)

                    # Obtener la cantidad del producto a partir del nombre del campo
                    cantidad_key = key.replace('producto', 'cantidad')
                    cantidad = int(request.POST[cantidad_key])

                    # Crear nuevo detalle de venta
                    detalle_venta = DetalleVenta()
                    detalle_venta.venta = venta
                    detalle_venta.producto = producto
                    detalle_venta.cantidad = cantidad
                    detalle_venta.precio_unitario = producto.precio
                    detalle_venta.subtotal = detalle_venta.precio_unitario * detalle_venta.cantidad
                    detalle_venta.save()

                    # Actualizar el total de la venta
                    venta.total += detalle_venta.subtotal

            # Guardar la venta con el total actualizado
            venta.save()

            # Redireccionar a la lista de ventas
            return redirect('/')
    else:
        # Obtener la lista de productos
        productos = Producto.objects.all()

        # Mostrar el formulario de venta
        return render(request, 'home.html', {'productos': productos})

@login_required
def eliminarventa(request, codigo_venta):
    venta = Venta.objects.get(codigo_venta=codigo_venta)
    venta.delete() #se encarga de borrarlos
    return redirect('/menu_Historial')

@login_required
def search_results(request): # esto lo saco de chatgpt xD 
    productos = Producto.objects.all()
    query_nombre = request.POST['query_nombre']
    query_rut = request.POST['query_rut']
    cliente = clientes.objects.filter(nombre__icontains=query_nombre, rut__icontains=query_rut)

    icono_count = 0 # estro es para cargar el contador que esta en la alerta
    Clientes = clientes.objects.all() # estro es para cargar el contador que esta en la alerta
    today = date.today() # estro es para cargar el contador que esta en la alerta
    for Clientes in Clientes: # estro es para cargar el contador que esta en la alerta
        if Venta.objects.filter(cliente = Clientes).order_by('-fecha_compra').first() is None:
            print("Cliente no posee Compras")
        else:
            ultima_fecha = Venta.objects.filter(cliente = Clientes).order_by('-fecha_compra').first()
            fecha_rgistrada = ultima_fecha.fecha_compra #Almacena solo la ultima fecha del cliente que se este recorriendo
            delta = today - fecha_rgistrada
            if delta.days >= 14:
                icono_count = icono_count + 1 
            else:
                icono_count = icono_count + 0
    return render(request, "core/registrar_Cliente.html", {'productos': productos, 'clientes_list': cliente,  "contador": icono_count})

@login_required
def regsitrar_Venta(request):
    return render(request, 'core/regsitrar_Venta.html')

@login_required
def ultima_Compra(request):
    return render(request, 'core/ultima_Compra.html')

@login_required
def Alerta(request):
    icono_count = 0
    productos = Producto.objects.all()
    lista_venta = [] #Lista la cual es la úlitma compra de cada Cliente
    Clientes = clientes.objects.all() #Llama a todos los clientes que se encuentra en models
    #Esta lista se utiliza para la funcion en la cual te trae la ultima fecha de venta registrada del cliente
    Clientes_list = clientes.objects.all() #Esto es para cargar los datos de los clientes a la venta 
    today = date.today()
    message = [] #Variable que almacena los mensajes de atraso de un cliente
    #Ej "Han pasado",delta.days ," Días desde que el cliente", Clientes.nombre,"no a realizado una compra")) 
    #Este for itera por cada cliente
    for Clientes in Clientes:
        if Venta.objects.filter(cliente = Clientes).order_by('-fecha_compra').first() is None:
            print("Cliente no posee Compras")
        else:
            ultima_fecha = Venta.objects.filter(cliente = Clientes).order_by('-fecha_compra').first()
            lista_venta.append(ultima_fecha)#Append inserta un dato en un arreglo, esto inserta la ultima compra realizada por el cliente
            fecha_rgistrada = ultima_fecha.fecha_compra #Almacena solo la ultima fecha del cliente que se este recorriendo
            delta = today - fecha_rgistrada
            if delta.days >= 14:
                message.append(("Han pasado",delta.days ," Días desde que el cliente", Clientes.nombre,"no a realizado una compra"))
                icono_count = icono_count + 1 
            else:
                print("No han pasado 2 semanas") 
    message.sort(reverse=True)
    return render(request, 'core/Alertas.html', {'productos': productos, "venta_list": lista_venta ,"clientes_lista": Clientes_list,'message': message, "contador": icono_count})




def Filtrar_fecha(request):
    query_fecha = request.POST['query_fecha']
    query_cliente = request.POST['query_nombre']
    productos = Producto.objects.all()
    ventas = Venta.objects.filter(fecha_compra__icontains=query_fecha, cliente__nombre__icontains=query_cliente).order_by('-fecha_compra')
    Clientes_list = clientes.objects.all() # esto es para cargar los datos de los clientes a la venta 
    detalles_ventas = []
    for venta in ventas:
        detalles_venta = []
        detalles = DetalleVenta.objects.filter(venta=venta)
        for detalle in detalles:
            producto = detalle.producto
            detalles_venta.append({
                'producto': producto.nombre,
                'precio': producto.precio,
                'cantidad': detalle.cantidad
                
            })
        detalles_ventas.append({
            'venta': venta,
            'detalles': detalles_venta
        })

    icono_count = 0 # estro es para cargar el contador que esta en la alerta
    Clientes = clientes.objects.all() # estro es para cargar el contador que esta en la alerta
    today = date.today() # estro es para cargar el contador que esta en la alerta
    for Clientes in Clientes: # estro es para cargar el contador que esta en la alerta
        if Venta.objects.filter(cliente = Clientes).order_by('-fecha_compra').first() is None:
            print("Cliente no posee Compras")
        else:
            ultima_fecha = Venta.objects.filter(cliente = Clientes).order_by('-fecha_compra').first()
            fecha_rgistrada = ultima_fecha.fecha_compra #Almacena solo la ultima fecha del cliente que se este recorriendo
            delta = today - fecha_rgistrada
            if delta.days >= 14:
                icono_count = icono_count + 1 
            else:
                icono_count = icono_count + 0
        
    return render(request, 'core/menu_Historial.html', {'productos': productos, "clientes_lista": Clientes_list, "venta_historial": detalles_ventas,  "contador": icono_count})



# registro de usuario
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Cambia 'home' por el nombre de tu vista de inicio
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})