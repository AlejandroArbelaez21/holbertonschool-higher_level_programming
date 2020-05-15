$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (apiTitles) {
      for (const apis of apiTitles.results) {
        $('UL#list_movies').append('<li>' + apis.title);
      }
    }
  });
});
