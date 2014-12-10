$(document).ready(function() {
  $('img').on('click', function(){
    var $this = $(this);
    // var input_value = $this.attr('id');
    //   alert ($this.attr('id'));
    //   $this.val($this.attr('value'));
    //   return false;
    // });
  });
  // $('#female_icon').on('click', function(){
  //   var gender_input = $('gender');
  //   $('#female_icon').click(function(){
  //       gender_input.val($(this).attr('value'));
  //   });
  // });

  // $('#male_icon').on('click', function(){
  //   alert("gender2 clicked");
  //   return $('#gender1 select option[value="female"]').html();
  // });

  $('.gender_icon').click(function(){
    var hinput = $(this);
    $('#gender_input').val(hinput.attr('value'));
    alert(hinput.attr('value'));
  });

  // var hinput = $('input[name="gender]');
  // $('.gender_icon').click(function(){
  //     hinput.val('test');
  //     alert(hinput.attr('value'));
  // });
});