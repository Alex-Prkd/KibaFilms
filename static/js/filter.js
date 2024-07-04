const selected = $(".selected");
const optionsContainer = $(".options-container");
const optionsList = $(".option");

$(selected).click(function(){
  $(this).parent().find(optionsContainer).toggleClass("active");
});

  $(optionsList).click(function(){
    var optionTitle = $(this).text();
    var optionValue = $(this).data();
    $(this).parents(".select-box").find(selected).text(optionTitle);
    $(this).parent(optionsContainer).removeClass("active");
    filterMovie(optionValue, ".sec-2__poster","filter-name");
  });

 function filterMovie(filterValue, selector, param) {
    $.post("/filter_films", {genre: filterValue["title"]})
    .done(function(response){
    $(selector).hide();
    if (response.movies !== null){
    var movies = response.movies
    $('.sec-2__content').remove().add("<div class='sec-2__content'></div>")
    var newElems = $("<div class='sec-2__content'></div>")
    for (movie of movies){
    newElems.append("<a href="+movie.href+" class='sec-2__poster'><div class='sec-2__poster-img'>\
    <img src='/static/img/banners/"+movie.image+"'/><div class='sec-2__poster-label'>114\
     / "+movie.episode_all+" серий</div></div><div class='sec-2__poster-desc>'<h3 class='sec-2__poster-title'>"+movie.ru_title+"</h3></div></a>")
    }
    $('.min-menu-movies').append(newElems);
    $(selector+'[data-'+param+'="'+filterValue+'"]').show();
    }
    })
    }