$('button').on('click', function(event){
  event.preventDefault();
  var element = $(this);
  $.ajax({
    url: '/like_target/',
    type: 'GET',
    data: { target_id: element.attr("data-id")},
    success: function(response){
      element.html(' ' + response)
    }
  });
});
