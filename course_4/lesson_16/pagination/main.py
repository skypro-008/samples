from flask import Flask, request, jsonify
from setup_db import db


app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///source.db"

db.init_app(app)


class ProductModel(db.Model):

    __tablename__ = "shop"

    id = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String)
    cat = db.Column(db.String)
    name = db.Column(db.String)
    kcal = db.Column(db.String)

    def as_dict(self):
        return {
            "pk": self.id, "icon": self.id, "cat": self.cat, "name": self.name, "kcal": self.kcal
        }


@app.route('/items/')
def show_items_paginated():

    # Получаем номер страницы (по умолчанию = 1)
    page = int(request.args.get('page', 1))

    # Устанавливаем количество на страницу (лучше вынести в константу или настройки приложения)
    items_per_page = 3

    result = db.session.query(ProductModel)
    result_paginated = db.paginate(result, page=page, per_page=items_per_page)

    return jsonify([product.as_dict() for product in result_paginated])



if __name__ == '__main__':

    host = '127.0.0.1'
    port = 8000

    print(f"open http://{host}:{port}/items/?page=1")
    app.run(host=host, port=port, debug=True)
