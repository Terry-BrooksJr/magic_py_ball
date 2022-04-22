import os

from flask import Flask, redirect, render_template, request, session, url_for
from flask_appbuilder import ModelRestApi, ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_sqlalchemy import SQLAlchemy
from forms import Question, Wisdom
from . import appbuilder, db
from app import app


@app.route('/', methods=['GET', 'POST'])
def home():
    form = Question()
    if request.method == 'GET':
        return render_template('index.html.jinja', form=form)
    else:
        recent_question = []


"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
