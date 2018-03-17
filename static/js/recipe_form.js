/*
When the form is submitted log a confirmation message. If
there are comments present on the recipe hide the no comments
section. Then call the create review method.
 */
$("#review_form").on('submit', function(event){
   event.preventDefault();
   console.log("form submitted");
   if ( $("#No_comments").length ) {
       $("#No_comments").hide();
   }
   create_review();
});

//author = django doc
function csrfSafeMethod(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

//author = django doc
/*
* Get the cookie for the csrftoken
*/
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
/*
* Attach the CSRF token to the post method otherwise django will reject the request.
* */
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain){
            xhr.setRequestHeader("X-CSRFToken", csrftoken)
        }
    }
});

/*
* Create the Review to send as JSON. The comment and the rating are sent
* upon a response the DOM is updated with the relevant information from the post request
* the comment will be updated along with username and timestamp.
* */
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
         $('.comment_section').prepend("<p>" + json.comment + "</p><p style='color:#2e9fb5;'><strong> - " + json.user + "</strong></p><p style=\"color:#C7C6CB; font-size: medium\"><i>" + json.date + "</i></p>");
      },
      error: function(xhr, errmsg, err){
          console.log(xhr.status + ": " + xhr.responseText);
      }
  });
};