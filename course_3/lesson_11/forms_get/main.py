import json
import os

from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)


@app.get('/')
def index():
    return render_template("form.html")


@app.get('/foo/')
def page_foo_get():
    return "Приняты данные" + request.values.get("my_login") + request.values.get("my_pass")


@app.post('/foo/')
def page_foo_post():
    return "Приняты данные" + request.values.get("my_login") + request.values.get("my_pass")


@app.post('/upload/')
def page_upload():

    first_name = request.values.get("first_name")
    last_name = request.values.get("last_name")

    file = request.files.get("avatar")
    filename = file.filename

    file_path = os.path.join(".", "uploads", filename)
    file.save(file_path)

    return f"Файл для пользователя {first_name} {last_name} загружен <a href='/uploads/{filename}'> Открыть </a>"


@app.get('/uploads/<path:path>')
@app.get('/uploads/<path:path>/')
def send_file(path):
    return send_from_directory("uploads", path)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
