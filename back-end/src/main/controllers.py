from flask import current_app

from models import Message
from database import db


def guest_book_GET(limit=10):
    with current_app.app_context():
        # make statement
        stmt = db.select(Message).order_by(Message.date.desc()).limit(limit)

        # execute query
        messages = db.session.execute(stmt).scalars()

        # return messages as list of dict (JSON)
        return [message.to_json() for message in messages]

def guest_book_POST(session):
    pass


def qu_code_POST(session):
    pass