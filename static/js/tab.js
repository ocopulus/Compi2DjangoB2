$('.tree-toggle').click(function () {	$(this).parent().children('ul.tree').toggle(200);
});
$(function(){
$('.tree-toggle').parent().children('ul.tree').toggle(200);
})

$(".nav-tabs").on("click", "a", function (e) {
        e.preventDefault();
        if (!$(this).hasClass('add-contact')) {
            $(this).tab('show');
        }
    })
    .on("click", "span", function () {
        var anchor = $(this).siblings('a');
        $(anchor.attr('href')).remove();
        $(this).parent().remove();
        $(".nav-tabs li").children('a').first().click();
    });

$('.add-contact').click(function (e) {
    e.preventDefault();
    var id = $(".nav-tabs").children().length; //think about it ;)
    var tabId = 'contact_' + id;
    $(this).closest('li').before('<li><a href="#contact_' + id + '">New Tab '+id+'</a> <span> x </span></li>');
    $('.tab-content').append('<div class="tab-pane" id=\'' + tabId + '\'>  <textarea class="textarea4 form-control" rows="10" id="txt'+id+'"></textarea>'+
    '<br/> <button type="button" class="btn btn-success" onclick="tabla(\'txt'+id+'\')">Success</button> '+
    '<button type="button" class="btn btn-success" onclick="saveTextAsFile(\'txt'+id+'\')">Guardar</button>'
    +'<button type="button" class="btn btn-success" onclick="buscarError(\'txt'+id+'\')">Validar Errores</button>'+' </div>');
   $('.nav-tabs li:nth-child(' + id + ') a').click();
   autoCompletado()
});

function autoCompletado(){
  $('.textarea4').textcomplete([
      { // tech companies
          words: ['si(){\n}sino{\n}', 'si(){\n}', 'crear objeto id ();', 'crear tabla id ();', 'crear procedimiento id (){\n}',
        'crear funcion id () tipo {\n}', 'retorno;', 'retorno EXP;','crear usuario nombre colocar password = "";',
        'usar NombreBD;', 'alterar tabla NombreTab agregar();', 'alterar objeto NombreObj agregar();',
        'alterar tabla NombreTab quitar LISTAIDS;', 'alterar objeto NombreObj quitar LISTAIDS;',
        'alterar usuario Nombreus cambiar password = "";', 'Eliminar ObjetoUsql id;', 'insertar en tabla id (VALORES);',
        'insertar en tabla id (LISTAIDS) valores (VALORES);', 'actualizar tabla NombreTab (LISTAIDS) valores (VALORES);',
        'actualizar tabla NombreTab (LISTAIDS) valores (VALORES) donde EXP;', 'borrar en tabla NombreTab;',
        'borrar en tabla NombreTab donde EXP;', 'seleccionar LISTAIDS de LISTAIDS donde EXP ordenar_por id (asc|desc);',
        'seleccionar LISTAIDS de LISTAIDS donde EXP;', 'seleccionar LISTAIDS de LISTAIDS ordenar_por id (asc|desc);',
        'otorgar permisos Id, Id.Id;', 'denegar permisos Id, Id.Id;'],
          match: /\b(\w{2,})$/,
          search: function (term, callback) {
              callback($.map(this.words, function (word) {
                  return word.indexOf(term) === 0 ? word : null;
              }));
          },
          index: 1,
          replace: function (word) {
              return word + ' ';
          }
      }
  ]);
}
autoCompletado();

function leerArchivo(e) {
  var archivo = e.target.files[0];
  if (!archivo) {
    return;
  }
  var lector = new FileReader();
  lector.onload = function(e) {
    var contenido = e.target.result;
    mostrarContenido(contenido);
  };
  lector.readAsText(archivo);
}

function mostrarContenido(contenido) {
  var txtare = $('#carga').val();
  var id = 'txt'+txtare;
  var elemento = document.getElementById(id);
  elemento.innerHTML = contenido;
}
document.getElementById('file-input').addEventListener('change', leerArchivo, false);

function tabla(t){
  var text = $('#'+t).val();
  //$('#'+t).val($.trim(text+' '+'hoal\n papu\n'));
  //console.log(text);
  var numero = t.replace(/\D/g,'');
  //console.log(t); //txtdeaccion
  //console.log('numero es: '+numero); //numerodel txt o div
  $.ajax({
       async:false,
       url: '/IDE/ajax/usql/',
       type: "GET", // http method
       data: { 'txt': text }, // data sent with the post request
       success: function(data) {
           //alert(data);
           //$('#contact_01').prepend().html($.trim(data));
           console.log(data);
           //$('#contact_'+numero).append($.trim(data));
       },
       failure: function(data) {
           alert('Got an error dude');
       }
     });

     $.ajax({
          async:false,
          url: '/IDE/ajax/tablas/',
          type: "GET", // http method
          success: function(data) {
              $('#SalidaD').append().html($('#SalidaD').html()+data);
          },
          failure: function(data) {
              alert('Got an error dude');
          }
        });

        $.ajax({
             async:false,
             url: '/IDE/ajax/ejecucion/',
             type: "GET", // http method
             success: function(data) {
                 var text = $('#txtejecucion').val();
                 text += '\n' + data;
                 $('#txtejecucion').val($.trim(text));
             },
             failure: function(data) {
                 alert('Got an error dude');
             }
           });
           $.ajax({
                async:false,
                url: '/IDE/ajax/mensajes/',
                type: "GET", // http method
                success: function(data) {
                    var text = $('#txtmensaje').val();
                    text += '\n' + data;
                    $('#txtmensaje').val($.trim(text));
                },
                failure: function(data) {
                    alert('Got an error dude');
                }
              });
              $.ajax({
                   async:false,
                   url: '/IDE/ajax/historial/',
                   type: "GET", // http method
                   success: function(data) {
                       var text = $('#txtHistorial').val();
                       text += '\n' + data;
                       $('#txtHistorial').val($.trim(text));
                   },
                   failure: function(data) {
                       alert('Got an error dude');
                   }
                 });
}

function saveTextAsFile(id)
{
    var textToWrite = document.getElementById(id).value;
//  create a new Blob (html5 magic) that conatins the data from your form feild
    var textFileAsBlob = new Blob([textToWrite], {type:'text/plain'});
// Specify the name of the file to be saved
    var fileNameToSaveAs = "codigo.usql";

    var downloadLink = document.createElement("a");
    downloadLink.download = fileNameToSaveAs;
    downloadLink.innerHTML = "My Hidden Link";
    window.URL = window.URL || window.webkitURL;
    downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
    downloadLink.onclick = destroyClickedElement;
    downloadLink.style.display = "none";
    document.body.appendChild(downloadLink);
    downloadLink.click();
}

function destroyClickedElement(event)
{
    document.body.removeChild(event.target);
}

function llenarMenus(){
  $.ajax({
       async:false,
       url: '/IDE/ajax/getUsuarios/',
       type: "GET", // http method
       success: function(data) {
         $('#usuarios').html($.trim(data));
       },
       failure: function(data) {
           alert('Got an error dude');
       }
     });
     $.ajax({
          async:false,
          url: '/IDE/ajax/getBD/',
          type: "GET", // http method
          success: function(data) {
            $('#BD').html($.trim(data));
          },
          failure: function(data) {
              alert('Got an error dude');
          }
        });
}
llenarMenus();

function buscarError(t){
  var text = $('#'+t).val();
  $.ajax({
       url: '/IDE/ajax/getErrores/',
       type: "GET", // http method
       data: { 'txt': text }, // data sent with the post request
       success: function(data) {
           $('#txtError').val($.trim(data));
       },
       failure: function(data) {
           alert('Got an error dude');
       }
     });
}
