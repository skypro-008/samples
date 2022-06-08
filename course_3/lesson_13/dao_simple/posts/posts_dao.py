from pprint import pprint as pp

import json

from exceptions import DataFileError
from post import Post

class PostsDAO:

    def __init__(self, path):
        self.path = path

    def _load(self):

        try:
            with open(self.path, "r", encoding="utf-8") as file:
                posts_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            raise DataFileError("Cannot get data from source")
        else:
            posts = [Post(**fields) for fields in posts_data]

        return posts

    def get_all(self):
        posts = self._load()
        return posts

    def get_by_pk(self, pk):
        """
        Получаем  пост по его pk
        """

        if type(pk) != int:
            raise ValueError("Post pk should be an int")

        posts = self._load()
        for post in posts:
            if post.pk == pk:
                return post

    def get_by_poster_name(self, name):
        """
        Получаем список постов по имени пользователя
        """

        if type(name) != str:
            raise ValueError("Poster name should be an str")

        name = name.lower()
        posts = self._load()
        matching_posts = [post for post in posts if post.poster_name.lower() == name]
        return matching_posts

    def search_in_content(self, substring):
        """
        Ищем текст в контенте постов и возвращаем подходящие посты
        """

        if type(substring) != str:
            raise ValueError("Substring name should be an str")

        substring = substring.lower()
        posts = self._load()
        matching_posts = [post for post in posts if substring in post.content.lower()]
        return matching_posts


posts_dao = PostsDAO("../data/posts_data.json")

pp(posts_dao._load())
