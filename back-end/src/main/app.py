from flask import Flask, jsonify
from flask_cors import CORS
from db import db

from datetime import date

from app_qrcode import app_qrcode
from app_guest_book import app_guest_book

from models import GUESTBOOKMESSAGE

app = Flask(__name__)
CORS(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)


with app.app_context():
    db.create_all()

    # Supprime toutes les entrées existantes dans la table
    GUESTBOOKMESSAGE.query.delete()

    # Ajoute des données d'exemple à la table
    example_data = [
        GUESTBOOKMESSAGE(author='John', text="Bonjour ! Merci de signer notre livre d'or.", date=date(2023, 12, 1)),
        GUESTBOOKMESSAGE(author='Alice', text="C'était une excellente expérience !", date=date(2023, 12, 2)),
        GUESTBOOKMESSAGE(author='Bob', text='Félicitations pour cet événement incroyable.', date=date(2023, 12, 3))
    ]

    db.session.bulk_save_objects(example_data)
    db.session.commit()


app.register_blueprint(app_guest_book)
app.register_blueprint(app_qrcode)


# Count Tables
@app.route('/count-tables')
def count_tables():
    try:
        with app.app_context():
            inspector = db.inspect(db.engine)
            table_names = inspector.get_table_names()
            num_tables = len(table_names)

            return jsonify({"num_tables": num_tables, "tables": table_names})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
