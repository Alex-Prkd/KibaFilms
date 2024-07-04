from config import Settings
from db.connection import create_db, create_session

engine = create_db(Settings.DATABASE_URI)
session_db = create_session(engine)