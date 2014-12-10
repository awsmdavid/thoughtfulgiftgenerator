$(document).ready(function() {

  //gender input selector using images
  $('.gender_icon').click(function(){
    var $this = $(this);
    var $this_class = $this.attr('class');
    var $this_id = $this.attr('value');
    //traverse node?
    //if image is selected...
    if ($(this).hasClass('on')) {
        $(this).removeClass('on').addClass('off');
    } else if ($(this).hasClass('off')) {
        $(this).removeClass('off');
    } else {
        $(this).addClass('off');
        alert($this.attr('class'));
    }
    $('#gender_input').val($this.attr('value'));
  });

  //age input selector using images
  $('.age_icon').click(function(){
    var $this = $(this);
    if ($(this).hasClass('on')) {
        $(this).removeClass('on').addClass('off');
    } else if ($(this).hasClass('off')) {
        $(this).removeClass('off');
    } else {
        $(this).addClass('off');
    }
    $('#age_input').val($this.attr('value'));
  });

  //gift category input selector using images
  $('.category_icon').click(function(){
    var $this = $(this);
    if ($(this).hasClass('on')) {
        $(this).removeClass('on').addClass('off');
    } else if ($(this).hasClass('off')) {
        $(this).removeClass('off');
    } else {
        $(this).addClass('off');
    }
    $('#category_input_tech').val($this.attr('value'));
  });

});