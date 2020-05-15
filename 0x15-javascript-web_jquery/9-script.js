$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (sayHello) {
      $('DIV#hello').append('<li>' + sayHello.hello);
    }
  });
});
