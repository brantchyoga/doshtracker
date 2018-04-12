

$(document).ready(()=>{
  console.log('loaded');
  $( function() {
      $( ".datepicker" ).datepicker({ dateFormat: 'yy-mm-dd' });
      $( ".datepicker" ).datepicker("setDate", new Date());
    } );
  // var elem = document.querySelector('.modal');
  // var instance = M.Modal.init(elem, options);
  $('.modal').modal();
})
