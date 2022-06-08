from flask import Flask, Blueprint

# Открывать ссылки

# /
# /one
# /one/two


app = Flask(__name__)

bp_parent = Blueprint('bp_parent', __name__)
bp_child = Blueprint('bp_child', __name__)


@app.route('/')
def index_app():
    return "Нулевой уровень"

@bp_parent.route('/')
def index_bp_1():
    return "Первый уровень"

@bp_child.route('/')
def index_bp_2():
    return "Второй уровень"

bp_parent.register_blueprint(bp_child, url_prefix="/two")
app.register_blueprint(bp_parent, url_prefix="/one")


print(app.url_map)



if __name__ == '__main__':
    app.run( debug=True, port=8000)
