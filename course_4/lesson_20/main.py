from unittest.mock import MagicMock

from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

db = SQLAlchemy(app)


# Конец подключения и настройки


class Product(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    price = db.Column(db.Integer)

    def __repr__(self):
        return f"Product({self.pk},{self.title})"


with app.app_context():
    Product.query.get_all = MagicMock(return_value=[])
    result = Product.query.get_all()

