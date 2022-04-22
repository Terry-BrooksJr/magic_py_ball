import os
from flask import Flask
from flask_cors import CORS
import redis
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from config import Config




db = SQLAlchemy()
sess = Session()
cors = CORS()


def create_app():
    """Construct the core flask_session_tutorial."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize Plugins
    db.init_app(app)
    sess.init_app(app)
    cors.init_app(app)

    with app.app_context():
        import routes

        # Create Database Models
        db.create_all()

    return app
