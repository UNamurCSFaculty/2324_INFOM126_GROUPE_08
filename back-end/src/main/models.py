from sqlalchemy import Column
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy


# db config
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)



# class Message(db.Model):
#     id_msg = Column(Integer, primary_key=True)
#     date: Mapped[Date]

