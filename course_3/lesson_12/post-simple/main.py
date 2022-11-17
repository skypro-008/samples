from crypt import methods

from flask import Flask, render_template, request

app = Flask(__name__)

form = """

<form method="post" action="boo" >
    <input name="field_1" />
    <input name="field_2" />
    <input type="submit" value="Отправить" />
</form>

"""


@app.route('/')
def page_form():
    return form


@app.post('/boo')
def page_process_request():
    field_1 = request.values.get("field_1")
    field_2 = request.values.get("field_2")
    return f"Форма получена {field_1=} {field_2=}"


@app.post("/enroll")
def page_enroll():
    name = request.values.get('name')
    phone = request.values.get('phone')
    group = request.values.get('group')

    return f"{name}{phone}{group}"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
