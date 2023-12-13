from flask import Blueprint, request, jsonify
from datetime import datetime
from db import db
from models import GUESTBOOKMESSAGE

app_guest_book = Blueprint('app_guest_book', __name__)

@app_guest_book.route("/guest-book", methods=["GET", "POST"])
def guest_book():
    if request.method == "GET":
          # Récupère les données de la table GUESTBOOKMESSAGE depuis la base de données
        entries = GUESTBOOKMESSAGE.query.all()
        entries_data = [{"author": entry.author, "text": entry.text, "date": entry.date} for entry in entries]
        return jsonify(entries=entries_data)

    elif request.method == "POST":
        data = request.json
        author = data.get("author")
        text = data.get("text")

        if author and text:
            # Ajouter une nouvelle entrée dans le livre d'or
            date = datetime.now()
            new_entry = GuestBookEntry(author=author, text=text, date=date)
            guest_book_entries.append(new_entry)

            return jsonify({'message': 'Message saved successfully!', 'entry': new_entry.__dict__})
        else:
            return jsonify({'error': 'Invalid data. Both author and text are required.'}), 400
