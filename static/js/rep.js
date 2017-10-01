function enviar(){
  var codigo = $('#txtcodigo').val();
  $.ajax({
       url: '/IDE/ajax/putoreporete/',
       type: 'GET', // http method
       data: { 'txt': codigo }, // data sent with the post request
       success: function(data) {
         console.log(data);
          $('#txtresultado').val(data);
       },
       failure: function(data) {
           alert('Got an error dude');
       }
     });

}
