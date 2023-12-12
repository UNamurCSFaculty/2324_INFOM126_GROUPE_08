from sqlalchemy import Integer, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from flask_sqlalchemy import SQLAlchemy


# ORM base class
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Message(db.Model):
    id_msg: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    date: Mapped[DateTime] = mapped_column(DateTime)
    text: Mapped[String] = mapped_column(String(500))


class Domain(db.Model):
    name: Mapped[String] = mapped_column(String(255), primary_key=True)
    count: Mapped[Integer] = mapped_column(Integer)

