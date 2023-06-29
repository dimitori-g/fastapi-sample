from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Phonetic(Base):
    __tablename__ = "phonetics"
    id = Column(Integer, primary_key=True, index=True)
    glyph = Column(String)
    phonetic = Column(String)
