from werkzeug.exceptions import NotFound
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import db


class User(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)

    userpic = Column(String, nullable=False)

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return str(self.username)

    def __repr__(self):
        return str(self)

    @classmethod
    def get_user_by_id(cls, user_id):
        user = cls.query.filter_by(id=user_id).one_or_none()
        if user is None:
            raise NotFound(f"User #{user_id} not found")
        return user
