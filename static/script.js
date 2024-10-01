// Tried all of these individually for the modal, even have jquery on my site.
// Hopefully one of these will make it work for you

$(window).load(function(){
    $("#myModal").modal('show');
});


$(window).on('load',function(){
    var delayMs = 1500; // delay in milliseconds
    
    setTimeout(function(){
        $('#myModal').modal('show');
    }, delayMs);
});   

$('.modal').modal('show');


$(document).ready(function(){
    $("#myModal").modal('show');
});


$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })
  