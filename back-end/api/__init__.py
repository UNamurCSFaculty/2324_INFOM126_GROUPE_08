from flask import Flask
from flask_cors import CORS

from api.endpoints import guest_book_blueprint, qrcode_blueprint
from api.database import db
from config import Database


def create_app(database_URI=Database.URI(), **kwargs):
    """ Application factory to create the app object. """

    # create Flask app
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = database_URI

    # add CORS header to back request
    CORS(app)

    # initialize the app with the extension
    db.init_app(app)

    # create tables if not created yet
    with app.app_context():
        db.create_all()

    # register blueprints
    app.register_blueprint(guest_book_blueprint)
    app.register_blueprint(qrcode_blueprint)

    # return app object
    return app
