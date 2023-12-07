from flask import Flask

from app_qrcode import app_qrcode
from app_guest_book import app_guest_book

app = Flask(__name__)
app.register_blueprint(app_guest_book)
app.register_blueprint(app_qrcode)