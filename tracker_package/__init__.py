from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from tracker_package.config import Config

db = SQLAlchemy()


def create_app(_configuration=Config):

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    from tracker_package.track.routes import track
    from tracker_package.entity.routes import entity

    app.register_blueprint(track)
    app.register_blueprint(entity)

    return app
