$( document ).ready(function() {

	
	//Remove address bar on Android
	window.addEventListener("load",function() {
	    setTimeout(function(){
	        window.scrollTo(0, 1);
	    }, 0);
	});

});

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
   console.log("Latitude: " + position.coords.latitude);
   console.log("Longitude: " + position.coords.longitude); 
}

//Do an ajax call to fetch the home venue stream
function listHomeStream(){

	$.ajax({
			
		method: "GET",
		url: '/getHomePosts/',
		success: function(data) {
			
			console.log(data);

			var output = '';

			$.each(data, function(i, venuePost){

				var blocktype = 
	   					((i % 3)===2) ? 'c':
	   					((i % 3)===1) ? 'b':
	   					'a';

	   			var latestUrl = venuePost.latestUrl;
		    	var locationID = venuePost.locationID;
		    	var venue = venuePost.venueName;
		    	

	    		output += '<div class="ui-block-' + blocktype + '">';
   				output += '<a href="#venuepage" data-transition="flip" data-role="button" onclick="listVenueStream(' + locationID + ',\'' + venue + '\')">';
   				output += '<img src="' + latestUrl + '">';
   				output += '</a>';
   				output += '<div class="photoCaption">';
   				//output += '<p class="distanceAway">3 mi away</p>';
   				output += '</div>';
   				output += '</div>';

		    });


			$("#homestream").html(output);
		}
			
	});//END AJAX function

}


function listVenueStream(locationID, venueName){

	$.ajax({
			
		method: "GET",
		url: '/getVenuePosts/',
		data: {'venueName': venueName, 'locationID' : locationID},
		success: function(data) {
			

			var output = '<div data-role="header" role="banner" class="ui-header ui-bar-inherit"><h1 id="venueHeader" class="ui-title" role="heading" aria-level="1"></h1><a href="#homestreampage" data-icon="bars" data-iconpos="notext" class="ui-link ui-btn-left ui-btn ui-icon-bars ui-btn-icon-notext ui-shadow ui-corner-all" data-role="button" role="button">Home</a></div>';

			$.each(data.posts, function(i, venuePost){

				var blocktype = 
	   					((i % 3)===2) ? 'c':
	   					((i % 3)===1) ? 'b':
	   					'a';

	   			var url = venuePost.mediaUrl;
	   			var captionText = venuePost.captionText;
	   			var numLikes = venuePost.numLikes;
	   			var numComments = venuePost.numComments;
	   			var createdUnixTime = venuePost.timestamp;


   				output += '<div class="ui-block-' + blocktype + '">';
				output += '<a href="#"><img src="' + url + '"></a>';
				output += '<div class="postInfo">';
				output += '<div class="postText">' + captionText + '</div>';
				output += '<div class="heartImg"><img style="border: 0;"></div>';
				output += '<div class="numLikes">' + numLikes +'</div>';
				output += '<div class="commentImg"><img style="border: 0;"></div>'
				output += '<div class="numComments">' + numComments + '</div>';
				output += '<div class="timeAgo"><span data-livestamp="' + createdUnixTime + '"></span></div>';
				output += '</div>';
				output += '</div>';


		    });// END for loop

			console.log("Output: " + output);

			$("#venuestream").html(output);
 			$("#venueHeader").html(venueName);

		}
			
	});//END AJAX function

}

