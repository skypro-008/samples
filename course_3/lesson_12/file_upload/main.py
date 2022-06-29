import os

from flask import Flask, render_template_string, request

app = Flask(__name__)

template = """

<form action="/upload" method="post" enctype="multipart/form-data">
    <input type="file" name="the_file">
    <input type="submit" value="Отправить файл">
</form>

"""


@app.route('/')
def index():
    return render_template_string(template)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        filename = f.filename

        f.save(os.path.join("uploads", f"nodot_{filename}"))\
        f.save(os.path.join(".", "uploads", f"dot_{filename}"))
        return "saved"


app.run()
