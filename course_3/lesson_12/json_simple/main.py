from flask import Flask, render_template, jsonify, Response, request

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

ws = [
    "платина", "стена", "халат", "блокнот", "косилка",
    "автобус", "базар", "биосфера", "грелка"
]


# @app.get('/')
# def index():


# result =

# response = Response(response="[1,2,3]", status=203, mimetype="application/json")

# result.headers.add_header("my_comment", "boo")


@app.get('/mirror/')
def page_mirror():
    json_data = request.get_json()
    json_data["processed"] = True
    return [True, True, False]


app.run()
