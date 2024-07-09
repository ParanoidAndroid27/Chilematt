function validarFormularioVenta() {
  // Validar el código de la factura
  var codigoFactura = document.getElementById('txtCodigo').value.trim();
  if (codigoFactura === '') {
    alert('Por favor, ingrese el código de la factura.');
    return false;
  }

  // Validar el cliente seleccionado
  var clienteSeleccionado = document.getElementById('my-select').value.trim();
  if (clienteSeleccionado === '' || clienteSeleccionado === 'input') {
    alert('Por favor, seleccione un cliente válido.');
    return false;
  }

  // Validar la fecha
  var fecha = document.getElementById('datefecha').value.trim();
  if (fecha === '') {
    alert('Por favor, seleccione una fecha.');
    return false;
  }

  // Validar al menos un producto agregado
  var productos = document.querySelectorAll('[id^="producto"]');
  if (productos.length === 0) {
    alert('Por favor, agregue al menos un producto.');
    return false;
  }

  // Validar la cantidad de cada producto
  for (var i = 0; i < productos.length; i++) {
    var cantidad = productos[i].querySelector('input[type="number"]').value.trim();
    if (cantidad === '' || cantidad <= 0) {
      alert('Por favor, ingrese una cantidad válida para el producto.');
      return false;
    }
  }

  // Si todas las validaciones pasan, se envía el formulario
  return true;
}

