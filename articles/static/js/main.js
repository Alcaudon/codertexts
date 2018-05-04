
/*Botón de ir arriba */


var clBackToTop = function() {
    
    var pxShow      = 400,
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


/* function onchange for select */
function changeOrder(estado) {
    var name = "order_by"
    var str = location.search;
    if (new RegExp("[&?]"+name+"([=&].+)?$").test(str)) {
        str = str.replace(new RegExp("(?:[&?])"+name+"[^&]*", "g"), "")
    }
    str += "&";
    str += name + "=" + estado;
    str = "?" + str.slice(1);
    // there is an official order for the query and the hash if you didn't know.
    location.assign(location.origin + location.pathname + str + location.hash)
};

/* para mantener el valor del select después de cargar la página */
var init = function (){
  //an ugly warning to users without localStorage support
  if(!window.localStorage){
    $('body').prepend('Sorry, you browser does not support local storage');
    return false;
  }
  var sel = $('select'),
      but = $('button');

  var clearSelected = function(){
      sel.find(':selected').prop('selected', false);
  }

  if(localStorage.getItem('pref')){
    var pref = localStorage.getItem('pref');
    clearSelected();
    //set the selected state to true on the option localStorage remembers
    sel.find('#' + pref).prop('selected', true);
  }

  var setPreference = function(){
    //remember the ID of the option the user selected
    localStorage.setItem('pref', sel.find(':selected').attr('id'));
  };

  var reset = function(){
    clearSelected();
    localStorage.setItem('pref', undefined);
  }

  sel.on('change', setPreference);
  but.on('click', reset);
};
if(document.URL.includes("?order_by")){
    $(document).ready(init);
}


/* cambio de favorito */
$(document).ready(function(){
    $("#favorito").click(function(){
        if($(this).hasClass("favorito")){
            $("#favorito").removeClass("favorito")
        }else{
            $("#favorito").addClass("favorito")
        }
    });
});

