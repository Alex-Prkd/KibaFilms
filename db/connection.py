from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_db(path_db):
    engine = create_engine(path_db, echo=False)
    return engine


def create_session(engine):
    session = sessionmaker(bind=engine)
    return session
