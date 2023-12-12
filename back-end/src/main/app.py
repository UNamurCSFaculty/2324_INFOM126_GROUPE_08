from flask import Flask

from app_qrcode import app_qrcode
from app_guest_book import app_guest_book
from models import db


# create Flask app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# initialize the app with the extension
db.init_app(app)

# register blueprints
app.register_blueprint(app_guest_book)
app.register_blueprint(app_qrcode)


# launch
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
