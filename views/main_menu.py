from flask import render_template

from db import session_db
from db.reader import GetMenu, AllMovies, MoviesTop, sorted_movies


def home():
    print(home.__name__)
    categories, status, types = GetMenu.get_menu(session_maker=session_db)
    movies = AllMovies(session_maker=session_db).get_movies()
    sort_movies = sorted_movies(movies)
    # # import locale
    # locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
    return render_template("index.html",
                           slider_menu=True,
                           categories=categories,
                           menu_status=status,
                           menu_type=types,
                           movies=sort_movies,
                           swiper_movies=movies,
                           all_films=movies)


def page_top():
    print(f"\n{page_top.__name__}\n")
    categories, status, types = GetMenu.get_menu(session_maker=session_db)
    movies = MoviesTop(session_maker=session_db).get_movies()
    all_movies = AllMovies(session_maker=session_db).get_movies()
    return render_template("top.html",
                           slider_menu=True,
                           image=["32282.jpg"],
                           categories=categories,
                           menu_status=status,
                           meny_type=types,
                           all_films=all_movies,
                           movies_list=movies)


def page_schedule():
    print(f"\n{page_schedule.__name__}\n")
    return render_template("404.html", context=page_schedule.__name__)


def page_bookmarks():
    print(f"\n{page_bookmarks.__name__}\n")
    return render_template("404.html", context=page_bookmarks.__name__)