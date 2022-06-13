from flask import Flask
# Импортируем экзепляр алхимии из отдельного файла
# Чтобы не создавать внутри app и не поймать цикл. импорт
from setup_db import db
# Импортируем модель из отдельного файла
from user_model import UserModel

app = Flask(__name__)

# Закидываем настройки, которые скоро использует алхимия
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Связываем базу данных и приложение
db.init_app(app)

# Связываем контекст с основным приложеним
# Чтобы не использовать with context

app.app_context().push()

# Вьюшка для демонстрации содержания базы

@app.route("/")
def page_show():

    # Получаем данные из таблички
    users = UserModel.query.all()
    # Показываем во вьюшке
    return "<br/>".join([f"{u.pk}  {u.first_name}  {u.last_name}" for u in users])

# Запускаем приложение тут

if __name__ == '__main__':
    app.run(debug=True, port=4000)
