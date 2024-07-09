function validarFormularioRCliente() {
    var rut = document.getElementById("txtRut").value;
    var nombre = document.getElementById("txtNombre").value;
    var direccion = document.getElementById("txtDireccion").value;
    var email = document.getElementById("txtEmail").value;
    var numero = document.getElementById("txtNumero").value;

    if (rut.trim() === "" || nombre.trim() === "" || direccion.trim() === "" || email.trim() === "" || numero.trim() === "") {
        alert("Por favor, complete todos los campos.");
        return false; // Evita que se envíe el formulario
    }

    // Validación del número de teléfono
    var telefonoRegex = /^[0-9]+$/; // Expresión regular para solo permitir dígitos
    if (!telefonoRegex.test(numero)) {
        alert("El número de teléfono solo puede contener dígitos.");
        return false; // Evita que se envíe el formulario
    }
    // Validación del correo electrónico
    var emailRegex = /^\S+@\S+\.\S+$/; // Expresión regular para validar correo electrónico
    if (!emailRegex.test(email)) {
        alert("Por favor, ingrese un correo electrónico válido.");
        return false; // Evita que se envíe el formulario
    }
    // Validación del RUT
    if (!validarRut(rut)) {
        alert("Por favor, ingrese un RUT válido.");
        return false; // Evita que se envíe el formulario
    }
    return true; // Permite el envío del formulario
}
function validarRut(rut) {
    rut = rut.replace(/\./g, ""); // Eliminar puntos del RUT
    rut = rut.replace(/-/g, ""); // Eliminar guiones del RUT

    var cuerpo = rut.slice(0, -1);
    var dv = rut.slice(-1).toUpperCase();

    if (cuerpo.length < 7) {
        return false;
    }

    var suma = 0;
    var multiplo = 2;

    for (var i = cuerpo.length - 1; i >= 0; i--) {
        suma += multiplo * cuerpo.charAt(i);
        multiplo++;

        if (multiplo === 8) {
            multiplo = 2;
        }
    }

    var resultado = 11 - (suma % 11);
    var dvCalculado = resultado === 11 ? "0" : resultado === 10 ? "K" : String(resultado);

    return dv === dvCalculado;
}
function validarBuscadores() {
    var nombreCliente = document.getElementsByName("query_nombre")[0].value.trim();
    var rutCliente = document.getElementsByName("query_rut")[0].value.trim();
  
    if (nombreCliente === "" && rutCliente === "") {
      alert("Por favor, ingresa al menos un término de búsqueda.");
      return false;
    }
    return true;
  }