from flask import Flask, render_template, request
app = Flask(__name__)


@app.get('/')
def index():
    return render_template("form.html")

@app.get('/foo/')
def process_form():

    return f"ГЕТ ВЬЮШКА"


@app.post('/foo/')
def process_post():
    return f"ПОСТ ВЬЮШКА"


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)

