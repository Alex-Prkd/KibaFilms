from dataclasses import dataclass
from datetime import datetime
from pprint import pprint

from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models import Categories, Movies, Status, Type, MovieCategory



def sorted_movies(movies):
    dict_movies = {}
    for movie in movies:
        try:
            if movie.adding_time == datetime.date(datetime.today()):
                dict_movies[f"Сегодня, {movie.adding_time}"].append(movie)
            else:
                dict_movies[str(movie.adding_time)].append(movie)
        except KeyError:
            if movie.adding_time == datetime.date(datetime.today()):
                dict_movies[f"Сегодня, {movie.adding_time}"] = [movie]
            else:
                dict_movies[str(movie.adding_time)] = [movie]
    return dict_movies


class GetMenu:
    @staticmethod
    def get_menu(session_maker):
        with session_maker() as session:
            categories = session.scalars(select(Categories)).all()
            status = session.scalars(select(Status)).all()
            types = session.scalars(select(Type)).all()
        return categories, status, types


class GetMoviesByStatus:
    def __init__(self, session_maker, status):
        self.session = session_maker
        self.status = status

    def get_movies(self, sorted_=False):
        with self.session() as session:
            status = session.scalar(select(Status).filter(Status.href == self.status))
            movies = session.scalars(
                select(Movies)
                .filter(Movies.status_id == status.id)
                .order_by(Movies.adding_time.desc())
            ).all()
        if sorted_:
            return sorted_movies(movies)
        return movies


class FilmsByGenre:
    def __init__(self, session_maker, genre):
        self.session = session_maker
        self.genre = genre

    def get_movies(self, sorted_=False):
        with self.session() as session:
            category = session.scalar(select(Categories).where(Categories.href == self.genre))
            movies = session.scalars(
                select(Movies, MovieCategory)
                .filter(MovieCategory.category_id == category.id)
                .filter(Movies.id == MovieCategory.movie_id)
                .order_by(Movies.adding_time.desc())
            ).all()
            if sorted_ is True:
                return sorted_movies(movies)
        return movies


class GetMovie:
    def __init__(self, session_maker, href):
            self.session = session_maker
            self.href = href

    def return_movie(self):
        with self.session() as session:
            movie = session.scalar(select(Movies).where(Movies.href == self.href))
        return movie


class AllMovies:
    def __init__(self, session_maker):
        self.session = session_maker

    def get_movies(self):
        with self.session() as session:
            movies = session.scalars(
                select(Movies).
                order_by(Movies.adding_time.desc())
            ).all()
        return movies


class MoviesByType:
    def __init__(self, session_maker, type_movie):
        self.session = session_maker
        self.type = type_movie

    def get_movies(self, sorted_=False):
        with self.session() as session:
            type_movie = session.scalar(select(Type).where(Type.href == self.type))
            movies = session.scalars(
                select(Movies).
                filter(Movies.type_id == type_movie.id).
                order_by(Movies.adding_time.desc())
            ).all()
        if sorted_:
            return sorted_movies(movies)
        return movies


class MoviesTop:
    def __init__(self, session_maker):
        self.session = session_maker

    def get_movies(self):
        with self.session() as session:
            session: Session
            movies = session.scalars(select(Movies).order_by(Movies.rating.desc())).all()
        return movies