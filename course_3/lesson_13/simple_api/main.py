import json
import random

from flask import Flask, jsonify, request

app = Flask(__name__)

data = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]


@app.get('/')
def index():
    page = int(request.args.get('page', 1))

    data_paginated = data[(page - 1) * 3:page * 3]
    return jsonify(data_paginated)


@app.get('/test/<pk>')
def test_args(pk):

    a = request.args.get('a')
    b = request.args.get('b')
    c = request.args.get('c')

    return jsonify([a, b, c]), 200

@app.post('/test/')
def test_json_data():

    data = request.get_json()

    with open("test.json", "w", encoding="utf-8") as file:
        data[1] = 2
        print(data, file=file)

    return jsonify([]), 201




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
