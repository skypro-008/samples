import os
from pprint import pprint as pp

# Импортируем наше DAO
from posts.posts_dao import PostsDAO

# Создаем экземпляр дао, натравливаем его на файл с данными
posts_dao = PostsDAO(os.path.join("data", "posts_data.json"))

# Для примера получаем и выводим все посты
pp(posts_dao.get_all())
