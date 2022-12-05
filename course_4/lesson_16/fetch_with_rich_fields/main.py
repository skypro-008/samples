# Начало подключения и настройки
# Эту часть мы будем опускать дальше в примерах эпизода

from flask import Flask
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


class Review(db.Model):

    pk = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)

    product_pk = db.Column(db.Integer, db.ForeignKey("product.pk"))
    product = db.relationship("Product")

    def __repr__(self):
        return f"Review({self.pk},{self.content})"


products = [
    Product(pk=1, title="Хлопья для завтрака", price=100),
    Product(pk=2, title="Шоколадное молоко", price=400),
    Product(pk=3, title="Овсяное печенье", price=400)
]

reviews = [
    Review(pk=1, content="Хорошие хлопья, мне понравилось!", product=products[0]),
    Review(pk=2, content="Вкусно очень, покупаю детям и сама пью!", product=products[1]),
    Review(pk=3, content="Обожаю печенье, ничего не могу с собой поделать! Ам м!", product=products[2])
]

with app.app_context():
    db.session.add_all(products + reviews)

def get_reviews_with_details(reviews):

    reviews_extended = []
    for review in reviews:
        reviews_extended.append(
            {
                "content": review.content,
                "product_name": review.product.title,
                "product_price": review.product.price,

            }
        )
    return reviews_extended

reviews_extended = get_reviews_with_details(reviews)

print(reviews_extended)
