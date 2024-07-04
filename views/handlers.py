from flask import Flask

from views.filter_menu import page_genre, page_status, page_type, page_movie, filter_by_genre
from views.main_menu import home, page_top, page_schedule, page_bookmarks


def menu(app: Flask):
    app.add_url_rule('/', view_func=home, methods=["GET", "POST"])
    app.add_url_rule("/top", view_func=page_top, methods=["GET", "POST"])
    app.add_url_rule("/raspisaniye", view_func=page_schedule, methods=["GET", "POST"])
    app.add_url_rule("/my-zakladki", view_func=page_bookmarks, methods=["GET", "POST"])
    app.add_url_rule("/filter_films", view_func=filter_by_genre, methods=["POST"])




def menu_filter(app: Flask):
    app.add_url_rule("/genre/<genre>", view_func=page_genre, methods=["GET", "POST"])
    app.add_url_rule("/new_genre", view_func=page_genre, methods=["GET", "POST"])
    app.add_url_rule("/status/<status>", view_func=page_status, methods=["GET", "POST"])
    app.add_url_rule("/type/<href>", view_func=page_type, methods=["GET", "POST"])
    # app.add_url_rule("/<id>/", view_func=page_movie, methods=["GET", "POST"])
    # app.add_url_rule("/<int:id>/<string:voice>", view_func=page_movie, methods=["GET", "POST"])


def movie_pages(app: Flask):
    app.add_url_rule("/<href_film>/", view_func=page_movie, methods=["GET", "POST"])