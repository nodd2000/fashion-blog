"""Наполнение тестовыми данными бд"""

from add_data import add_some_data
from models.base import db
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import config


if __name__ == '__main__':
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
    db.Model.metadata.create_all(engine)
    session = Session(bind=engine)
    add_some_data(session)
    session.close()
