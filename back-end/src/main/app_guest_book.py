from flask import Blueprint, request, jsonify
from datetime import datetime
from db import db
from models import GUESTBOOKMESSAGE

app_guest_book = Blueprint('app_guest_book', __name__)

@app_guest_book.route("/guest-book", methods=["GET", "POST"])
def guest_book():
    if request.method == "GET":
        entries = GUESTBOOKMESSAGE.query.all()
        entries_data = [{"author": entry.author, "text": entry.text, "date": entry.date} for entry in entries]
        return jsonify(entries=entries_data)

    elif request.method == "POST":
            data = request.json
            author = data.get("author")
            text = data.get("text")

            if author and text:
                date = datetime.now()
                new_entry = GUESTBOOKMESSAGE(author=author, text=text, date=date)
                db.session.add(new_entry)
                db.session.commit()

                return jsonify({'message': 'Message saved successfully!', 'entry': {"author": new_entry.author, "text": new_entry.text, "date": new_entry.date}})
            else:
                return jsonify({'error': 'Invalid data. Both author and text are required.'}), 400