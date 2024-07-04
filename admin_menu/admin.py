from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from db.models import Categories, Movies, Voice, Status, Type


def create_admin(app: Flask, session):
    app.config["FLASK_ADMIN_SWATCH"] = "cerulean"
    admin = Admin(app=app, name="KibaSite", template_mode="bootstrap3")

    class TestView(ModelView):
        column_list = [Movies.ru_title, "status.title", "type.title",
                       "voice.title"]
        column_labels = {
            "ru_title": "Фильм",
            "status.title": "Статус",
            "type.title": "Тип",
            "voice.title": "Озвучка",
            "categories": "Категория",
            "status": "Статус",
            "type": "Тип",
            "voices": "Озвучка",
        }       # Поменять все значиния при создании новой записи (зайти в саму запись)
        column_filters = ("categories", "status", "type", "voices", )


    admin.add_view(ModelView(Categories, session=session()))
    admin.add_view(TestView(Movies, session=session()))
    admin.add_view(ModelView(Voice, session=session()))
    admin.add_view(ModelView(Status, session=session()))
    admin.add_view(ModelView(Type, session=session()))