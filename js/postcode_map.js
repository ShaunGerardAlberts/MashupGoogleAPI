var map;
var markers = [];

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -26.715, lng: 137.064},
    zoom: 4
  });
 }

function removeExistingMarkers() {
  for (let i = 0; i < markers.length; i++) {
    markers[i].setMap(null);
  };
}

 $(document).ready(function(){

    $("#form1").submit(function(event){
      event.preventDefault();
      removeExistingMarkers();
      //process the form
      var postCode = $('#form1').serializeArray()[0].value;
      // get the marker for the supplied postcode, and add to existing map
      $.ajax( {
        url: "http://localhost:8080/getlocation?postcode=" + postCode,
        method: "get",
        dataType: "json"
      })
      .done( function(location) {
        //have the needed details, make marker
        marker = new google.maps.Marker({
          map: map,
          position: {lat: parseFloat(location.lat), lng: parseFloat(location.lon)},
          title: location.name
        });
        markers.push(marker);
      })
      .fail(function(error) {
        alert("An Error Occured");
      })
      $("#store_postcode").val("");
    })
    
  });