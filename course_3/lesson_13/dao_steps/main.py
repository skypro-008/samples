from flask import Flask, jsonify
from posts_dao import PostsDAO

POST_PATH = "posts_data.json"

app = Flask(__name__)
app.config["JSON_AS_ASCII"] =  False

# создавать объект доступа к постам
post_dao = PostsDAO(POST_PATH)


@app.route('/')
def index():
    # получать все посты
    posts = post_dao.get_all()
    posts_as_dicts = [post.as_dict() for post in posts]
    return jsonify(posts_as_dicts)


@app.get('/posts/<int:pk>/')
def get_post_by_pk(pk):
    """ Получить пост по его номеру """
    post = post_dao.get_by_pk(pk)
    return jsonify(post.as_dict())


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
