$( document ).ready(function() {

	posts = {};

	$('.insta-likes').each(function(i, obj) {
	   //console.log(obj.closest('article').id + "->" + obj.innerHTML);
	   posts[obj.closest('article').id] = parseInt(obj.innerHTML);
	});

	console.log(sortDict(posts));

});

function sortDict(dict){
	
	// Create items array
	var items = Object.keys(dict).map(function(key) {
	    return [key, dict[key]];
	});

	// Sort the array based on the second element
	items.sort(function(first, second) {
	    return second[1] - first[1];
	});

	return items;

}
