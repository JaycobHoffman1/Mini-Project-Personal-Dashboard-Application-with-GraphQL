from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Movie(Base):
    __tablename__ = 'movies'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String(255), nullable=False)
    director: Mapped[str] = mapped_column(db.String(255), nullable=False)
    year: Mapped[int] = mapped_column(db.Integer, nullable=False)
    genre_id: Mapped[int] = mapped_column(db.ForeignKey('genres.id'), nullable=False)

class Genre(Base):
    __tablename__ = 'genres'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)