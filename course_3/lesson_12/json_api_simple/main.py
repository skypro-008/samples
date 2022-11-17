
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/<pk>')
def index(pk):

    data = {
        "1": "has_content",
        "2": None
    }

    content = data[pk]

    if content is None:
        return jsonify({"status": "no content"}), 204
    else:
        return jsonify({'status': "OK", "content": content}), 200


@app.post('/create')
def page_create():
    data = request.get_json()
    data["name"] = data["name"].upper()
    data["phone"] = str(data["phone"])
    return jsonify(data)


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)

