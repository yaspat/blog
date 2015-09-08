/*
   Little snippet to make IPython notebook output/input  cells alternate
   between hidden and visible states.
*/  

$(document).ready(function(){
  $(".output_wrapper").click(function(){
      $(this).prev('.input_hidden').slideToggle();
  });
})

$(document).ready(function(){
  $(".input").click(function(){
      $(this).next('.output_hidden').slideToggle();            
  });
})


