from werkzeug.exceptions import NotFound
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import db


class Theme(db.Model):
    __tablename__ = "themes"

    id = Column(Integer, primary_key=True)
    theme_en = Column(String(30), nullable=False)
    theme_ru = Column(String(30), nullable=False)

    posts = relationship("Post", back_populates="theme")

    def __str__(self):
        return str(self.theme_en)

    def __repr__(self):
        return str(self)

    @classmethod
    def get_theme_by_id(cls, theme_id):
        theme = cls.query.filter_by(id=theme_id).one_or_none()
        if theme is None:
            raise NotFound(f"Theme #{theme_id} not found")
        return theme
