from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class UserModel(db.Model):
    """Модель пользователя"""
    __tablename__ = 'user'

    pk = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String, nullable=True)


# Все оборачиваем в контекст
with app.app_context():
    # Пересоздаем базу данных
    db.drop_all()
    db.create_all()

    # # Создаем пользователей
    user_1 = UserModel(pk=1, first_name="Алиса")
    user_2 = UserModel(pk=2, first_name="Денис")

    #  Загружаем все в базу данных
    db.session.add_all([user_1, user_2])
    db.session.commit()
