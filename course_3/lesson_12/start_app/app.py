from flask import Flask
from create_db import db # Вся магия происходит тут
from model import User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def index():
    user = User(first_name="Алиса")
    return user.first_name


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)

