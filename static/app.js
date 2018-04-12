

$(document).ready(()=>{
  console.log('loaded');
  $( function() {
      $( "#datepicker" ).datepicker();
    } );
  // var elem = document.querySelector('.modal');
  // var instance = M.Modal.init(elem, options);
  $('.modal').modal();
})
