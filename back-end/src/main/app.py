from flask import Flask

from endpoints import guest_book_blueprint, qrcode_blueprint
from models import db


# create Flask app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# initialize the app with the extension
db.init_app(app)

# register blueprints
app.register_blueprint(guest_book_blueprint)
app.register_blueprint(qrcode_blueprint)


# launch
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
