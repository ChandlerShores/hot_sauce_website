$(document).ready(function(){
  $("#carouselExampleIndicators").carousel();

  // Enable the prev and next buttons
  $(".carousel-control-prev").click(function(){
    $("#carouselExampleIndicators").carousel("prev");
  });
  $(".carousel-control-next").click(function(){
    $("#carouselExampleIndicators").carousel("next");
  });
});
