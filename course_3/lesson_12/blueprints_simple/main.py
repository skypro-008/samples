from flask import Flask, render_template
from bp_one.views import bp_one
from bp_two.views import bp_two

app = Flask(__name__)

app.register_blueprint(bp_one, url_prefix="/one")
app.register_blueprint(bp_two, url_prefix="/two")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
