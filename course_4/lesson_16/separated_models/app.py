from flask import Flask
# Импортируем экзепляр алхимии из отдельного файла
# Чтобы не создавать внутри app и не поймать цикл. импорт
from setup_db import db
# Импортируем модель из отдельного файла
from user_model import UserModel

app = Flask(__name__)

# Закидываем настройки, которые скоро использует алхимия
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Связываем базу данных и приложение
db.init_app(app)

# Связываем контекст с основным приложеним
# Чтобы не использовать with context

app.app_context().push()

# Создаем все таблицы
# В реальном коде это нужно вынести
db.drop_all()
db.create_all()

# Добавляем экземплярку модели
user_1 = UserModel(pk=1, first_name="Jane", last_name="Doe")

# Пишем в базу
db.session.add(user_1)
db.session.commit()

print(user_1)
