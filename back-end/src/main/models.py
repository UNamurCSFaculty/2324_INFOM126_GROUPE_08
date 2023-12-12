from sqlalchemy import Integer, DateTime, String
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy


#
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Message(db.Model):
    id_msg = mapped_column(Integer, primary_key=True)
    date = mapped_column(DateTime)
    text = mapped_column(String(500))


class Domain(db.Model):
    name = mapped_column(String(255), primary_key=True)
    count = mapped_column(Integer)

