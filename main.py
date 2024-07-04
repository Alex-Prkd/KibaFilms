from flask import Flask

import config
from admin_menu.admin import create_admin
from db import session_db
from views.handlers import menu, menu_filter, movie_pages


def main():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = config.Settings.SECRET_KEY

    menu(app)
    menu_filter(app)
    movie_pages(app)
    create_admin(app=app, session=session_db)
    app.run(debug=True)


if __name__ == "__main__":
    main()