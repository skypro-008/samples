# Начало подключения и настройки

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

# Конец подключения и настройки

class Product(db.Model):

    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    price = db.Column(db.Integer)

    def __repr__(self):
        return f"Product({self.pk},{self.title})"

class Review(db.Model):

    pk = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)

    product_pk = db.Column(db.Integer, db.ForeignKey(Product.pk))
    product = db.relationship(Product, foreign_keys=[product_pk])

    def __repr__(self):
        return f"Review({self.pk},{self.content})"

review_1 = db.session.query(Review).get(1)

print(review_1)
print(review_1.product)


