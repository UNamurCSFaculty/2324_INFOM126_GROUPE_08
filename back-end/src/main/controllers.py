from flask import current_app

from src.main.models import db, Message


def guest_book_GET(limit=10):
    with current_app.app_context():
        stmt = db.select(Message).order_by(Message.date.desc())

        messages = db.execute(stmt)

        return [message.to_json() for message in messages]

def guest_book_POST(session):
    pass


def qu_code_POST(session):
    pass