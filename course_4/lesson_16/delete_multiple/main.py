from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

# Создаем модельку

class Product(db.Model):

    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    price = db.Column(db.Integer)

    def __repr__(self):
        return f"Product({self.pk},{self.title})"


# пересоздаем базу
db.drop_all()
db.create_all()

# наполняем базу тестовыми записями
product_1 = Product(pk=1, title="Продукт 1", price=100)
product_2 = Product(pk=2, title="Продукт 2", price=200)
product_3 = Product(pk=3, title="Продукт 3", price=300)
db.session.add_all([product_1, product_2, product_3])
db.session.commit()

# создаем запрос на получение нескольких штук по ключу
items = db.session.query(Product).filter(Product.pk.in_([1,2,3]))
items.delete()

# проверяем, действительно ли записи удалились
products_after_deletion = db.session.query(Product).all()
print(products_after_deletion)

