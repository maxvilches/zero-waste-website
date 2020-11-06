$("#register_form").validate({
    rules: {
        nombre: {
            required: true,
            minlength: 3,
            maxlength: 80
        },
        apellido: {
            required: true,
            minlength: 3,
            maxlength: 80
        },
        email: {
            required: true,
            email: true,
        },
        usuario: {
            required: true,
            minlength: 8,
        },
        password: {
            required: true,
            minlength: 8,
        }
    }
})

$("#insumos_form").validate({
    rules: {
        nombre: {
            required: true,
            minlength: 3,
            maxlength: 120
        },
        precio: {
            required: true,
            min: 1
        },
        descripcion: {
            minlength: 3,
            maxlength: 200
        }
      
    }
})

$("#guardar").click(function() {

    // verificar datos *

    if(!$("#register_form").valid()) {
        return
    }

    let rut = $("#rut").val()
    let nombre = $("#nombre").val()
    let apellido = $("#apellido").val()
    let email = $("#email").val()
    let fecha_nac = $("#fecha_nac").val()
    let usuario = $("#usuario").val()
    let password = $("#password").val()
})
