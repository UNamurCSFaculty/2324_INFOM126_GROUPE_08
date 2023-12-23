from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy


# ORM base class
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
