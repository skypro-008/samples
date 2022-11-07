from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return {"status": "ok"}, 200



# Обрати внимание, мы не запускаем приложения

