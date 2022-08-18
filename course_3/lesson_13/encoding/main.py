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

    product_pk = db.Column(db.Integer, db.ForeignKey(Product.pk))
    product = db.relationship(Product)

    def __repr__(self):
        return f"Review({self.pk},{self.content})"


# Пересоздаем БД в целях демонстрации
db.drop_all()
db.create_all()

# Добавляем продукт и отзыв к нему

product_1 = Product(pk=1, title="Хлопья для завтрака", price=100)
review_1 = Review(pk=1, content="Хорошие хлопья", product=product_1)

# Сохраняем в базе данных

db.session.add(product_1)
db.session.add(review_1)
db.session.commit()

review_1 = db.session.query(Review).get(1)

print(review_1)
print(review_1.product)
