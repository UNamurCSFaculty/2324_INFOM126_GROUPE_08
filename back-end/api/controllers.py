from flask import current_app
from datetime import datetime
from io import BytesIO
from qrcode import QRCode, constants

from api.models import Message
from api.database import db


def guest_book_GET(limit=10):
    with current_app.app_context():
        # make statement
        stmt = db.select(Message).order_by(Message.date.desc()).limit(limit)

        # execute query
        messages = db.session.execute(stmt).scalars()

        # return messages as list of dict (JSON)
        return {"entries": [message.to_json() for message in messages]}


def guest_book_POST(author: str, text: str):
    with current_app.app_context():
        # make statement
        new_message = Message(author=author, text=text, date=datetime.now())

        # execute query
        db.session.add(new_message)
        db.session.commit()

        # return new message created as dict (JSON)
        return {
            "message": "New message successfully saved !",
            "entry": new_message.to_json()
        }


def qrcode_POST(url: str):
    qr = QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img_buffer = BytesIO()
    img.save(img_buffer)
    img_buffer.seek(0)

    return img_buffer

