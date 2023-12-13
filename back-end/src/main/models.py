from datetime import datetime
from db import db

class GUESTBOOKMESSAGE(db.Model):
    author = db.Column(db.String(50), primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __init__(self, author, text, date=None):
        self.author = author
        self.text = text
        if date is None:
            date = datetime.now()
        self.date = date
