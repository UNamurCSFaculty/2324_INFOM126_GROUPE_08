from flask import Flask

from endpoints import guest_book_blueprint, qrcode_blueprint
from models import db, Domain
from configs import Database, API


# create Flask app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = Database.URI

# initialize the app with the extension
db.init_app(app)

# create tables if not created yet
with app.app_context():
    db.create_all()

# register blueprints
app.register_blueprint(guest_book_blueprint)
app.register_blueprint(qrcode_blueprint)


# launch
if __name__ == '__main__':
    app.run(host=API.HOST, port=API.PORT)
