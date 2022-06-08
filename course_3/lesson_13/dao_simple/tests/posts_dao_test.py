import os

import pytest

from course_3.lesson_13.dao_simple.posts.posts_dao import PostsDAO
from course_3.lesson_13.dao_simple.posts.post import Post


class TestPostsDAO:

    @pytest.fixture()
    def posts_dao(self):
        posts_dao_instance = PostsDAO(os.path.join("tests", "mock_posts.json"))
        return posts_dao_instance

    def test_get_all(self, posts_dao):

        posts = posts_dao.get_all()
        assert type(posts) == list
        assert type(posts[1]) == Post
        assert len(posts) == 8
