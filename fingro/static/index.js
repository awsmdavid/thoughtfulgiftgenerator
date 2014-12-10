$(document).ready(function() {

  //gender input selector using images
  $('.gender_icon').click(function(){
    var $this = $(this);
    $('#gender_input').val($this.attr('value'));
  });

  //age input selector using images
  $('.age_icon').click(function(){
    var $this = $(this);
    $('#age_input').val($this.attr('value'));
  });

  //gift category input selector using images
  $('.category_icon').click(function(){
    var $this = $(this);
    $('#category_input_tech').val($this.attr('value'));
  });

});