# Импортируем приложение и объект алхимии
from app import app, db

# Достаем модельку чтобы создать ползателя
from user_model import UserModel

from data_to_import import LIST_OF_USERS

# Удаляем и заново создаем таблицы
db.drop_all()
db.create_all()

# Создаем модельки
users = [UserModel(**user_data) for user_data in LIST_OF_USERS]

# Если хотим проверить, что внутри
[print(u.pk, u.first_name) for u in users]

# Закидываем модели в сессию
db.session.add_all(users)

# Пишем в базу изменения
db.session.commit()
