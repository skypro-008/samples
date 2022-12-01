from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

db = SQLAlchemy(app)

# Конец подключения и настройки


class User(db.Model):

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genre_pk = db.Column(db.Integer, db.ForeignKey("genre.pk"))
    genre = db.relationship("Genre")

    def __repr__(self):
        return f"User({self.pk},{self.name}, {self.genre})"


# Здесь мы создаем модель
class Genre(db.Model):

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # здесь необходимый метод repr
    def __repr__(self):
        return f"Genre({self.pk},{self.name})"


# Здесь мы тестируем
genre_1 = Genre(pk=1, name="action")
user_1 = User(pk=1,name="a", genre=genre_1)

print(user_1)



