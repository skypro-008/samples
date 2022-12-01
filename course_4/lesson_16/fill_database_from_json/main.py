import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    """Модель пользователя"""
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    url = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"User({self.id}, {self.first_name}, {self.url})"


# вытаскиваем данные из файла
with open("data.json") as file:
    data = json.load(file)


with app.app_context():

    # Пересоздаем базу
    db.drop_all()
    db.create_all()
    # создаем экземпляры пользователей
    users = [User(**user_data) for user_data in data]
    # добавляем в сессию и коммитим
    db.session.add_all(users)
    db.session.commit()

    print(db.session.query(User).all())
