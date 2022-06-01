from flask import Flask

# Импортируем функцию из модуля
from utils import foo

app = Flask(__name__)

# Задаем конфиг, который потом будем использовать
# Можем также импортировать конфиг из файла или

app.config["GREETING"] = "Добро пожаловать к нам!"


@app.route('/')
def greetings_page():
    """ Выьюшка, выводит приветствие, хранящееся в конфиге """
    greeting = foo()
    return greeting


app.run(debug=True)

