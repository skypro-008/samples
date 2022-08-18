# Начало подключения и настройки
# Эту часть мы будем опускать дальше в примерах эпизода

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

    reviews = db.relationship("Review")

    def __repr__(self):
        return f"Product({self.pk},{self.title})"

class Review(db.Model):

    pk = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)

    product_pk = db.Column(db.Integer, db.ForeignKey("product.pk"))
    product = db.relationship("Product", back_populates="reviews")

    def __repr__(self):
        return f"Review({self.pk},{self.content})"

product_1 = Product(pk=1, title="Хлопья для завтрака", price=100)
review_1 = Review(pk=1, content="Хорошие хлопья", product=product_1)
review_2 = Review(pk=2, content="Мне понравилось!", product=product_1)

print(product_1.reviews)
