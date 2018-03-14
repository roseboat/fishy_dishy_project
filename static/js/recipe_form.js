$("#review_form").on('submit', function(event){
   event.preventDefault();
   console.log("form submitted");
   create_review();
});

function csrfSafeMethod(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

//author = django doc
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken')

//author django doc
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain){
            xhr.setRequestHeader("X-CSRFToken", csrftoken)
        }
    }
});

function create_review(){
  $.ajax({
     url: "",
      type: "POST",
      dataType: "JSON",
      data: { "comment" : $('#id_comment').val(), "rating": $('#id_rating').val()},
      success: function(json){
         $('#id_comment').val('');
         $('#id_rating').val('');
         console.log(json);
         $('ul').prepend("<li>" + json.comment + "</li><li>" + json.rating + "</li><li>" + json.user + "</li>")
      },
      error: function(xhr, errmsg, err){
          console.log(xhr.status + ": " + xhr.responseText);
      }
  });
};