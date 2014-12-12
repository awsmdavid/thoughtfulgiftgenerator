$(document).ready(function() {

//TODO: create toggle function to avoid this horrible crap

  //gender input selector using images
  $('.gender_icon').click(function(){
    var $this = $(this);
    var $gender_icon_class = $('.gender_icon');
    var $this_id = $this.attr('value');

    // alert($this.attr('value'));
    if ($(this).hasClass('off')){
     $this.removeClass('off');
     $this.addClass('on');
     $gender_icon_class.not("#"+$this.attr("id")).removeClass('on');
     $gender_icon_class.not("#"+$this.attr("id")).addClass('off');
    }
    //first time any option is selected (nothing has a class)
    else {
     $gender_icon_class.not("#"+$this.attr("id")).addClass('off');
     $this.addClass('on');
    }
    //set value of gender input
    $('#gender_input').val($this.attr('value'));
  });

// $( ".myClass" ).css( "border", "3px solid red" );


  //age input selector using images
  $('.age_icon').click(function(){
    var $this = $(this);
    var $age_icon_class = $('.age_icon');
    //if another input is already selected
    if ($(this).hasClass('off')){
     $this.removeClass('off');
     $this.addClass('on');
     $age_icon_class.not("#"+$this.attr("id")).removeClass('on');
     $age_icon_class.not("#"+$this.attr("id")).addClass('off');
    }
    //first time any option is selected (nothing has a class)
    else {
     $age_icon_class.not("#"+$this.attr("id")).addClass('off');
     $this.addClass('on');
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