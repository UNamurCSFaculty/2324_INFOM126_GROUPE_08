from flask import current_app
from datetime import datetime

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
    if author is None or text is None:
        return "Invalid request. Both author and text are required.", 400

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


def qr_code_POST(session):
    pass
