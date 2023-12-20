from flask import Flask
from flask_cors import CORS

from api.endpoints import guest_book_blueprint, qrcode_blueprint
from api.database import db


def create_app(database_URI, debug=False, **kwargs):
    """ Application factory to create the app object. """

    # create Flask app
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = database_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = debug

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

