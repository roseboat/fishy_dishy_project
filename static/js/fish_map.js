
// function of searching for location
// saving the latitude and longitude
function searchLocation(result) {
            var latitude = result.geometry.location.lat();
            var longitude = result.geometry.location.lng();

            var current = {lat:latitude , lng: longitude};

            displayMap(current);
        }

    // uses address (input by user)
    // to get latitude and longitude  values
    function getLatitudeLongitude(callback, address) {

        address = address
        // Initialize the Geocoder
        geocoder = new google.maps.Geocoder();
        if (geocoder) {
            geocoder.geocode({
                             'address': address
                             }, function (results, status) {
                             if (status == google.maps.GeocoderStatus.OK) {
                             callback(results[0]);
                             }
                             });
        }
    }

    // get user input (address or postal code)
    var button = document.getElementById('btn');

    button.addEventListener("click", function () {
                            // passes address to getLatitudeLongitude() function to convert into lat and long values
                            var address = document.getElementById('address').value;
                            getLatitudeLongitude(searchLocation, address)
                            });


                            // get the location of the user's current position
                            // using geolcation
                            function getLocation() {
                                if (navigator.geolocation) {
                                    navigator.geolocation.getCurrentPosition(initMap);
                                } else {
                                    x.innerHTML = "Geolocation is not supported by this browser.";
                                }
                            }

    // initialises map using user's default latitude and longitude co-ordinates
    // passes co-ordinates to displayMap() function
    function initMap(position) {
        var latitude=position.coords.latitude;
        var longitude= position.coords.longitude;

        var current = {lat:latitude , lng: longitude};

        displayMap(current);
    }

    // displaying map using set latitude and longitude values
    // default is user's geolocation
    // or newly searched location
    var map;
    var infowindow;
    function displayMap (current) {

        map = new google.maps.Map(document.getElementById('map'),
                                  { center: current, zoom: 11 });
                                  
                                  infowindow = new google.maps.InfoWindow();
                                  var service = new google.maps.places.PlacesService(map);
                                  // search radius set to 20000
                                  // searches for fishmongers in the area
                                  service.nearbySearch({ location: current, radius: 20000,
                                                       keyword: "fishmonger", }, callback);
    }

    // function to create a marker for each result found
    // when searching for fishmongers in nearby area
    function callback(results, status) {
        if (status === google.maps.places.PlacesServiceStatus.OK) {
            for (var i = 0; i < results.length; i++) {
                createMarker(results[i]);
            }
        }
    }

    // function for creating markers on map to locate
    // places of interest (fishmongers)
    function createMarker(place) {
        var placeLoc = place.geometry.location;
        var marker = new google.maps.Marker({
                                            map: map,
                                            position: place.geometry.location
                                            });

                                            google.maps.event.addListener(marker, 'click', function() {
                                                                          infowindow.setContent(place.name);
                                                                          infowindow.open(map, this);
                                                                          });
    }

// make getLocation() function available on load
$(document).ready(function (){


    getLocation();
    $(".btn").click(function () {
        var query = $("#address").val();
    })
});