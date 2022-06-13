# Модель импортирует объект алхимии
from setup_db import db


class UserModel(db.Model):

    pk = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
