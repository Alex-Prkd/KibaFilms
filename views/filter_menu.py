from pprint import pprint

from flask import render_template, request, jsonify, session

from db import session_db
from db.models import Movies
from db.reader import FilmsByGenre, GetMoviesByStatus, GetMenu, AllMovies, GetMovie, MoviesByType


def page_genre(genre):
    if request.method == "POST":
        print("method post ----> {}".format(page_genre.__name__))
    categories, status, types = GetMenu().get_menu(session_maker=session_db)
    all_movies = AllMovies(session_maker=session_db).get_movies()
    movies_genre = FilmsByGenre(session_maker=session_db, genre=genre)
    movies_for_page = movies_genre.get_movies(sorted_=True)
    return render_template("genre.html",
                           movies=movies_for_page,
                           image=["32282.jpg"],
                           slider_menu=True,
                           swiper_movies=set(all_movies),
                           categories=categories,
                           menu_status=status,
                           menu_type=types,
                           all_films=all_movies)


def page_status(status):
    categories_menu, status_menu, types_menu = GetMenu.get_menu(session_maker=session_db)
    all_movies = AllMovies(session_maker=session_db).get_movies()
    movies = GetMoviesByStatus(session_maker=session_db, status=status).get_movies(sorted_=True)
    print(page_status.__name__)
    return render_template("status.html",
                           image=["32282.jpg"],
                           movies=movies,
                           slider_menu=True,
                           categories=categories_menu,
                           menu_status=status_menu,
                           menu_type=types_menu,
                           all_films=all_movies)


def page_type(href):
    categories_menu, status_menu, types_menu = GetMenu.get_menu(session_maker=session_db)
    all_movies = AllMovies(session_maker=session_db).get_movies()
    movies = MoviesByType(session_maker=session_db, type_movie=href).get_movies(sorted_=True)
    print(page_type.__name__)
    return render_template("type.html",
                           image=["32282.jpg"],
                           slider_menu=True,
                           categories=categories_menu,
                           menu_status=status_menu,
                           menu_type=types_menu,
                           movies=movies,
                           all_films=all_movies)


def page_movie(href_film, voice=None):
    categories_menu, status_menu, types_menu = GetMenu.get_menu(session_maker=session_db)
    movie: Movies = GetMovie(session_maker=session_db, href=href_film).return_movie()
    description = {"short": movie.description_short, "all": movie.description_all}
    """ 
    Убрать целую кучу этого списка и передать объект movie
    """
    return render_template("movie-page.html",
                           categories=categories_menu,
                           menu_status=status_menu,
                           menu_type=types_menu,
                           title_ru=movie.ru_title,
                           title_en=movie.en_title,
                           status=movie.status.title,
                           date_status=movie.year,
                           episode_last="*****",
                           episode_all=movie.episode_all,
                           season=movie.season,
                           type=movie.type,
                           genres=movie.categories,
                           studio=movie.studio,
                           voices=movie.voices,
                           description=description,
                           rating=movie.rating,
                           count_rating=movie.count_rating,
                           banner=f"img/banners/{movie.image}",
                           movie_id=movie.id
                           )


def filter_by_genre():
    if request.method == "POST":
        movies = FilmsByGenre(session_maker=session_db, genre=request.form["genre"]).get_movies()
        if len(movies) == 0:
            movies = None
        else:
            session["filter_movies"] = {"genre": request.form["genre"]}
            movies = [movie.to_dict(only=("href", "image", "ru_title", "episode_all")) for movie in movies]
        return jsonify({"movies": movies})



