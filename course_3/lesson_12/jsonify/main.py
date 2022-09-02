import json

from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    a = jsonify([1,2,3])
    a = json.dumps([1,2,3])
    print(type(a))
    print(a)
    return a

if __name__ == '__main__':

  app.run(host='127.0.0.1', port=8000, debug=True)

