from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class UserModel(db.Model):

    __tablename__ = 'user'

    pk = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"User({self.pk}, {self.first_name}, {self.last_name})"


class OrderModel(db.Model):

    __tablename__ = 'order'
    pk = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)

    owner_pk = db.Column(db.Integer, ForeignKey("user.pk"))
    performer_pk = db.Column(db.Integer, ForeignKey("user.pk"))

    owner = db.relationship("UserModel", foreign_keys=[owner_pk])
    performer = db.relationship("UserModel", foreign_keys=[performer_pk])


db.drop_all()
db.create_all()

user_1 = UserModel(pk=1, first_name="Алиса")
user_2 = UserModel(pk=2, first_name="Денис")

order = OrderModel(pk=1, description="..", owner = user_1, performer = user_2)

db.session.add_all([user_1, user_2, order])

db.session.commit()

order = db.session.query(OrderModel).get(1)

print(order.owner)
print(order.performer)
