from flask import Flask, render_template
from utils import get_tags


app = Flask(__name__)


@app.route('/')
def index():
    content = "#раз два #три четыре #пять"
    return get_tags(content)



if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)


