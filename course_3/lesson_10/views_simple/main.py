from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index_get():
    return render_template("index_for_get.html")


@app.route('/', methods=['POST'])
def index_post():
    return render_template("index_for_post.html")

from flask import url_for


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)


