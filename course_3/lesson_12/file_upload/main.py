# Демонстрация двух способов сохранения файла из формы

# Запусти приложение.
# Перейди к форме.
# Отправь файл.
# Загляни в папку uploads

import os
from flask import Flask, render_template_string, request, send_from_directory

app = Flask(__name__)

template = """

<form action="/upload" method="post" enctype="multipart/form-data">
    <input type="file" name="the_file">
    <input type="checkbox" name="use_dot"> Добавить точку
    <input type="submit" value="Отправить файл">
</form>

"""

@app.route('/')
def index():
    """
    Вьюшка показывает форму
    """
    return render_template_string(template)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        filename = f.filename

        if request.values.get("use_dot", False):
            f.save(os.path.join(".", "uploads", f"dot_{filename}"))
        else:
            f.save(os.path.join("uploads", f"nodot_{filename}"))

        return "saved"


@app.get('/uploads/<path:path>')
def show_uploaded(path):
    return send_from_directory('uploads',path)


app.run(port=8081)
