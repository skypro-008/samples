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

    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255))
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    role = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    user_order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    user_offer_id = db.Column(db.Integer, db.ForeignKey("offer.id"))


class Order(db.Model):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(150), nullable=False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    address = db.Column(db.String(255))
    price = db.Column(db.Float)
    customer_id = db.Column(db.Integer, db.ForeignKey("offer.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    offers = db.relationship("Offer")


class Offer(db.Model):
    __tablename__ = "offer"

    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    order_id = db.Column(db.Integer)
    executor_id = db.Column(db.Integer)

    user_offer = db.relationship("User")


user_1 = User(id=1, first_name="User_1", email="foo_1@foo_1.com", )
user_2 = User(id=2, first_name="User_2", email="foo_2@foo_2.com", )
order_1 = Order(name='Order_1', description='Foot', address="NY", price=5.5, customer_id=user_1, executor_id=user_2)
order_2 = Order(name='Order_2', description='FWt', address="LA", price=10.5, customer_id=user_2, executor_id=user_2)

print(f'Order: {order_1.customer_id.first_name}, User: {user_1.first_name}')
print(f'Order: {order_2.executor_id.first_name}')
