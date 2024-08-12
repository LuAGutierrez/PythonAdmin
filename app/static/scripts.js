// Boton para ir a tareas //
$(document).ready(function() {
    // jQuery
    $('#tareas').on('click', function() {
        window.location.href = '/tareas';
    });

    $('#tickets').on('click', function() {
        window.location.href = '/tickets';
    });

    $('#filtro').on('change', function() {
        var selectedValue = $(this).val(); // Obtiene el valor seleccionado del elemento 'filtro'.
        window.location.href = `/tickets?estado=${selectedValue}`; // Redirige con el filtro aplicado como parámetro.
    });


// Manejo modal de tickets //

    var modal = $('#modales');
    var btn = $('#crear');
    var span = $('.cerrar');

// jQuery: Asigna un manejador de eventos al botón que muestra el modal.
    btn.on('click', function() {
        modal.show(); // Muestra el modal al hacer clic en el botón.
    });

    // jQuery: Asigna un manejador de eventos al botón de cierre para ocultar el modal.
    span.on('click', function() {
        modal.hide(); // Oculta el modal al hacer clic en el botón de cierre.
    });

    // jQuery: Asigna un manejador de eventos global para cerrar el modal si se hace clic fuera de él.
    $(window).on('click', function(event) {
        if ($(event.target).is(modal)) {
            modal.hide(); // Oculta el modal si el clic ocurre fuera del modal.
        }
    });

    // Fin manejo modal tickets //

    // Manejo mensajes flash //

    // jQuery: Maneja los mensajes flash, ocultándolos después de un tiempo y eliminándolos del DOM.
    var msgflash = $('.flash-msg').first();
    if (msgflash.length) {
        setTimeout(function() {
            msgflash.fadeTo(500, 0, function() {
                $(this).remove(); // Elimina el mensaje después de que se desvanece.
            });
        }, 3000); // Espera 3 segundos antes de iniciar el desvanecimiento.
    }
        
});
    // Manejo modal tareas