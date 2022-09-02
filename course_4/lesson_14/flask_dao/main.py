from flask import Flask, render_template
from dao import SampleDAO

app = Flask(__name__)

# создаем общее соединение
simple_dao = SampleDAO(connection)


@app.route('/')
def index():
    data = simple_dao.get_all()
    return str(data)



app.run(host='127.0.0.1', port=8000, debug=True)




