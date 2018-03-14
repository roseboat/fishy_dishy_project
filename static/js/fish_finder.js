$(document).ready(function (){
   $('#radioButtons input').on('change', function () {

        var query = $('input[name="options"]:checked', '#radioButtons').val();

        if (query === "all") {
            $(".fish").show();
        } else {
            $(".fish").hide();
            var selector = "." + query;
            $(selector).show();
        }
   });



   $('.btn').click(function () {
      var num = $(this).val();
      function myFunction(num) {
        num = "." + num;
        $(".fish").hide();
        $(num).show();
    }
    myFunction(num);
   });

});