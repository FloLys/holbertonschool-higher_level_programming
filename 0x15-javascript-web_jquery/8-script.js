const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (data) {
	$.each(data, function (index, item) {
		$('UL#list_movies').append('<li>' + item.title + '</li>');
	})
});