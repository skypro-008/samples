from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

data = [
    {"pk": 1, "name": "milk", "unit_price": 50},
    {"pk": 2, "name": "sugar", "unit_price": 30},
    {"pk": 3, "name": "cookies", "unit_price": 50},
    {"pk": 4, "name": "corn-flakes", "unit_price": 70},
    {"pk": 5, "name": "nutella", "unit_price": 125}
]

loger = logging.getLogger('basic')
loger.setLevel(logging.DEBUG)
filehandler = logging.FileHandler('log_one.txt', encoding='utf-8')
loger.addHandler(filehandler)
filehandler.setLevel(logging.DEBUG)


@app.route('/products/')
def hello_world():
    loger.debug('Запрос /products')
    return jsonify(data)


@app.route('/products/<int:pk>/')
def products(pk):
    for item in data:
        if item['pk'] == pk:
            loger.debug('Запрос /products/pk')
            return jsonify(item)
    loger.error('Ошибко 404')
    return "Error 404"


@app.post('/products/')
def create_product():
    new_product = request.json
    data.append(new_product)
    loger.debug('Запрос ПОСТ /products')
    return jsonify(new_product)


if __name__ == '__main__':
    app.run()
