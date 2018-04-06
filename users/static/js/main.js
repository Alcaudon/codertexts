
/*Botón de ir arriba */


var clBackToTop = function() {
    
    var pxShow      = 500,
        goTopButton = $(".go-top")

    // Show or hide the button
    if ($(window).scrollTop() >= pxShow) goTopButton.addClass('link-is-visible');

    $(window).on('scroll', function() {
        if ($(window).scrollTop() >= pxShow) {
            if(!goTopButton.hasClass('link-is-visible')) goTopButton.addClass('link-is-visible')
        } else {
            goTopButton.removeClass('link-is-visible')
        }
    });
};


/*Mostrar popup de búsqueda*/

var clSearch = function(nombreCapa, nombreBoton) {
    
    var wrap = $(nombreCapa),
        botonCerrar = wrap.find('.header__overlay-close'),
        searchTrigger = $(nombreBoton),
        siteBody = $('body');


    searchTrigger.on('click', function(e) {
        
        e.preventDefault();
        e.stopPropagation();
    
        var $this = $(this);
    
        siteBody.addClass('is-visible');
        setTimeout(function(){
            wrap.find('.first-field').focus();
        }, 100);
    
    });

    botonCerrar.on('click', function(e) {

        var $this = $(this);
    
        e.stopPropagation(); 
    
        if(siteBody.hasClass('is-visible')){
            siteBody.removeClass('is-visible');
            setTimeout(function(){
                wrap.find('.first-field').blur();
            }, 100);
        }
    });

    wrap.on('click', function(e) {
        if( !$(e.target).is('.first-field') ) {
            botonCerrar.trigger('click');
        }
    });
        

};



//Función para el ojo de la password

$(".toggle-password").click(function() {
    
      $(this).toggleClass("fa-eye fa-eye-slash");
      var input = $($(this).attr("toggle"));
      if (input.attr("type") == "password") {
        input.attr("type", "text");
      } else {
        input.attr("type", "password");
      }
});

//Calendario de formulario


/*
$('#fecha').datepicker({
    format: "dd/mm/yyyy",
    language: "es",
    orientation: "bottom auto"
});
*/

//Ejecución de las funciones
clBackToTop();
clSearch('#capaBuscar', '.capa-buscador');