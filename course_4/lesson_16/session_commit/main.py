# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

app = Flask(__name__)
# app.config.from_object(Configuration)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    pk = db.Column(db.Integer, primary_key=True, autoincrement="auto")


with app.app_context():

    db.create_all()

    # Используем первый способ:

    user_1 = User(pk=1)

    with db.session.begin():
        db.session.add_all([user_1])

    print(db.session.query(User).all())

    # Используем второй способ:

    user_2 = User(pk=2)
    db.session.add_all([user_2])

    print(db.session.query(User).all())


