import json
from post_model import PostModel

class PostsDAO:

    def __init__(self, path):
        self.path = path

    def _load_data(self):
        """ Внутренний метод который загружает данные"""
        with open(self.path, encoding='utf-8') as file:
            data = json.load(file)
            instances = [PostModel(**post_data) for post_data in data]
        return instances

    def get_all(self):
        """ Возвращает полный список постов """
        data = self._load_data()
        return data

    def get_by_pk(self, pk):
        """ Возвращаем экземпляр с нужным pk если такой есть"""
        all_posts = self._load_data()
        for post in all_posts:
            if post.pk == pk:
                return post

    def get_by_poster_name(self, poster_name):
        """ Возвращаем экземпляры по автору"""
        poster_name = poster_name.lower()
        all_posts = self._load_data()
        return [post for post in all_posts if post.poster_name == poster_name]

#
# posts_dao = PostsDAO("posts_data.json")
#
# # all_posts = posts_dao.get_all()
# posts_by_name = posts_dao.get_by_poster_name("leo")
#
# print(posts_by_name)
