from flask import Flask, render_template
app = Flask(__name__)


class DataCorruptedError(Exception):
    pass


def foo():
    raise DataCorruptedError("booomm")


@app.route('/')
def index():
    foo()


@app.errorhandler(DataCorruptedError)
def bar(error):
        return f"Протизошла ошибка {error}"


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)

