$(document).ready(function() {
  $('img').on('click', function(){
    var $this = $(this);
      alert ($this.attr('id'));
    });

});
