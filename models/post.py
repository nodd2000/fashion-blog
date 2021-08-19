from werkzeug.exceptions import NotFound
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from models import db
from models.user import User
from models.theme import Theme


class Post(db.Model):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(50), nullable=False)
    html = Column(Text, nullable=False)
    main_photo = Column(Text, nullable=False)
    theme_id = Column(Integer, ForeignKey('themes.id'), nullable=False)
    is_published = Column(Boolean, nullable=False, default=False, server_default="0")

    user = relationship(User, back_populates="posts")
    theme = relationship(Theme, back_populates="posts")

    def __str__(self):
        return str(self.title)

    def __repr__(self):
        return str(self)

    @classmethod
    def get_post_by_id(cls, post_id):
        post = cls.query.filter_by(id=post_id).one_or_none()
        if post is None:
            raise NotFound(f"Post #{post_id} not found")
        return post
