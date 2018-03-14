function searchLocation(result) {
            var latitude = result.geometry.location.lat();
            var longitude = result.geometry.location.lng();

            var current = {lat:latitude , lng: longitude};

            displayMap(current);
        }

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

    var button = document.getElementById('btn');

    button.addEventListener("click", function () {
                            var address = document.getElementById('address').value;
                            getLatitudeLongitude(searchLocation, address)
                            });



                            function getLocation() {
                                if (navigator.geolocation) {
                                    navigator.geolocation.getCurrentPosition(initMap);
                                } else {
                                    x.innerHTML = "Geolocation is not supported by this browser.";
                                }
                            }

    function initMap(position) {
        var latitude=position.coords.latitude;
        var longitude= position.coords.longitude;

        var current = {lat:latitude , lng: longitude};

        displayMap(current);
    }

    var map;
    var infowindow;
    function displayMap (current) {

        map = new google.maps.Map(document.getElementById('map'),
                                  { center: current, zoom: 11 });

                                  infowindow = new google.maps.InfoWindow();
                                  var service = new google.maps.places.PlacesService(map);
                                  service.nearbySearch({ location: current, radius: 20000,
                                                       keyword: "fishmonger", }, callback);
    }

    function callback(results, status) {
        if (status === google.maps.places.PlacesServiceStatus.OK) {
            for (var i = 0; i < results.length; i++) {
                createMarker(results[i]);
            }
        }
    }

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
$(document).ready(function (){


    getLocation();
    $(".btn").click(function () {
        var query = $("#address").val();
        alert(query);
    })
});