from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

db = SQLAlchemy(app)

# Конец подключения и настройки

favorite_genres = db.Table('favorite_genres',
    db.Column('user_id', db.Integer, db.ForeignKey('user.pk')),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.pk'))
)

class User(db.Model):

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genres = db.relationship('Genre', secondary=favorite_genres)

    def __repr__(self):
        return f"User({self.pk},{self.name}, {self.genres})"


class Genre(db.Model):

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f"Genre({self.pk},{self.name})"




genre_1 = Genre(pk=1, name="action")
genre_2 = Genre(pk=2, name="adventure")

user_1 = User(pk=1,name="a", genres=[genre_1, genre_2])

print(user_1)



