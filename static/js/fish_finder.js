    /*
    Method which is called whenever a radio button on the page has been clicked.
    Gets the value of the radio button, if it is 'all' it shows all of the .fish div sections.
    Otherwise, it hides all of the .fish divs and shows the one corresponding to the radio button's value.
     */

$(document).ready(function () {
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

    /*
    Similar to before. If a sustainability button is clicked, this method gets its value and
    hides all of the .fish divs, showing those that correspond to the number clicked.
     */

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