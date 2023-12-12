from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from app_qrcode import app_qrcode
from app_guest_book import app_guest_book


# db config
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)



app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)
# register blueprint
app.register_blueprint(app_guest_book)
app.register_blueprint(app_qrcode)





# launch
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
