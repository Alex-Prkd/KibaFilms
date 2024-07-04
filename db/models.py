from datetime import datetime


from sqlalchemy import Column, Integer, String, ForeignKey, Date, DATE
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_serializer import SerializerMixin

Base = declarative_base()


class MovieCategory(Base):
    __tablename__ = "association_movie_category"

    movie_id = Column(Integer, ForeignKey("movie.id"), primary_key=True)
    category_id = Column(Integer, ForeignKey("category.id"), primary_key=True)


class MovieVoice(Base):
    __tablename__ = "association_movie_voice"
    movie_id = Column(Integer, ForeignKey("movie.id"), primary_key=True)
    voice_id = Column(Integer, ForeignKey("voice_movie.id"), primary_key=True)


class Movies(Base, SerializerMixin):
    __tablename__ = "movie"

    id = Column(Integer, primary_key=True)
    ru_title = Column(String)
    en_title = Column(String)
    href = Column(String, unique=True)
    description_short = Column(String)
    description_all = Column(String)
    image = Column(String)
    episode_all = Column(Integer)
    season = Column(String)
    studio = Column(String)
    rating = Column(Integer)
    count_rating = Column(String)
    adding_time = Column(Date, default=datetime.date(datetime.today()))
    categories = relationship("Categories",
                              secondary="association_movie_category",
                              back_populates="movies",
                              lazy="immediate"
                              )

    status_id = Column(Integer, ForeignKey("status.id"))
    status = relationship("Status", back_populates="movie", lazy="immediate")
    year = Column(String) # что-то типа DATE для того чтоб выбировать год выпуска
    type_id = Column(Integer, ForeignKey("type_movie.id"))
    type = relationship("Type", back_populates="movie", lazy="immediate")
    voices = relationship("Voice",
                          secondary="association_movie_voice",
                          back_populates="movies",
                          lazy="immediate")
    #   ="immediate" - хочу узнать




class Categories(Base, SerializerMixin):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    title = Column(String(16))
    href = Column(String)
    movies = relationship("Movies",
                          secondary="association_movie_category",
                          back_populates="categories",
                          lazy="immediate")

    def __repr__(self):
        return self.title


class Status(Base, SerializerMixin):
    __tablename__ = "status"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    href = Column(String)
    movie = relationship("Movies", back_populates="status", lazy="immediate")

    def __repr__(self):
        return self.title


class Voice(Base, SerializerMixin):
    __tablename__ = "voice_movie"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    href = Column(String)
    movies = relationship("Movies",
                          secondary="association_movie_voice",
                          back_populates="voices",
                          lazy="immediate")

    def __repr__(self):
        return self.title


class Type(Base, SerializerMixin):
    __tablename__ = 'type_movie'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    href = Column(String)
    movie = relationship("Movies", back_populates="type", lazy="immediate")

    def __repr__(self):
        return self.title

