from flask import Flask

from utils import foo

app = Flask(__name__)

app.config["GREETING"] = "Добро пожаловать к нам!"


@app.route('/')
def greetings_page():
    """ Выьюшка, выводит приветствие, хранящееся в конфиге """
    greeting = foo()
    return greeting


app.run(debug=True)

