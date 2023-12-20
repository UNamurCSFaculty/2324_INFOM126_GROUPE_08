from sqlalchemy import Integer, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from api.database import db


class Message(db.Model):
    id_message: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    date: Mapped[DateTime] = mapped_column(DateTime)
    author: Mapped[String] = mapped_column(String(30))
    text: Mapped[String] = mapped_column(String(500))

    def to_json(self):
        return {
            "id": self.id_message,
            "date": str(self.date),
            "author": self.author,
            "text": self.text
        }


class Domain(db.Model):
    name: Mapped[String] = mapped_column(String(255), primary_key=True)
    count: Mapped[Integer] = mapped_column(Integer)

    def to_json(self):
        return {
            "domain": self.name,
            "count": self.count
        }
