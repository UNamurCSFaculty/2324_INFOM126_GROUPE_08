from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
 #TODO: ADD SQLAlchemy et ajouter dans une variable db


#class GuestBookMessage(db.Model):
#    __tablename__ = 'GUESTBOOKMESSAGE'
#   author = db.Column(db.String(50), primary_key=True)
#   text = db.Column(db.Text, nullable=False)
#   date = db.Column(db.Date, nullable=False)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/get_guest_book")
def get_guest_book():
    messages_guest_book = GuestBookMessage.query.all()

    for entry in messages_guest_book:
        print(entry.serialize())

    return jsonify(messages_guest_book=[entry.serialize() for entry in messages_guest_book])


@app.route("/post_guest_book", methods=['POST'])
def post_guest_book():
    data = request.get_json()

    new_entry = GuestBookMessage(
        author=data['author'],
        text=data['text'],
    )

    db.session.add(new_entry)
    db.session.commit()

    return jsonify({'date': new_entry.date.strftime('%Y-%m-%d')})

if __name__ == "__main__":
    app.run(debug=True)