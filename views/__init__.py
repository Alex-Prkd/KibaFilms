from flask import Flask


# def menu(app: Flask):
#     app.add_url_rule('/', view_func=home, methods=["GET", "POST"])
#     # app.add_url_rule("/<int:id>/", view_func=movie, methods=["GET", "POST"])
#     app.add_url_rule("/top/", view_func=page_top, methods=["GET", "POST"])
#     app.add_url_rule("/raspisaniye/", view_func=page_schedule, methods=["GET", "POST"])
#     app.add_url_rule("/serialy/", view_func=page_series, methods=["GET", "POST"])
#     app.add_url_rule("/my-zakladki/", view_func=page_bookmarks, methods=["GET", "POST"])
#
#
#
# def menu_filter(app: Flask):
#     app.add_url_rule("/genres/", view_func=page_genres, methods=["GET", "POST"])
#     app.add_url_rule("/status/", view_func=page_status, methods=["GET", "POST"])
#     app.add_url_rule("/type/", view_func=page_type, methods=["GET", "POST"])
