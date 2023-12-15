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

def guest_book_POST(message: Message):
    pass
    # with current_app.app_context():
        # make statement

        # execute query

        # return new message created as dict (JSON)

    # data = request.json
    # author = data.get("author")
    # text = data.get("text")
    #
    # if author and text:
    #     date = datetime.now()
    #     new_entry = GUESTBOOKMESSAGE(author=author, text=text, date=date)
    #     db.session.add(new_entry)
    #     db.session.commit()
    #
    #     return jsonify({'message': 'Message saved successfully!',
    #                     'entry': {"author": new_entry.author, "text": new_entry.text, "date": new_entry.date}})
    # else:
    #     return jsonify({'error': 'Invalid data. Both author and text are required.'}), 400


def qr_code_POST(session):
    pass