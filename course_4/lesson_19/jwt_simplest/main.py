import calendar
import datetime

from flask import Flask, render_template, request, abort
import jwt

secret = 's3cR$eT'
algo = 'HS256'

app = Flask(__name__)


@app.route('/')
def index():

    data = request.headers['Authorization']
    token = data.split("Bearer ")[-1]
    try:
        jwt.decode(token, secret, algorithms=[algo])
    except Exception as e:
        print("JWT Decode Exception", e)
        return "", 401

    return "", 200


@app.route('/auth')
def func_name():

    data = {'username': 'myname', 'role': 'user'}

    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    data["exp"] = calendar.timegm(min30.timetuple())
    return jwt.encode(data, secret, algorithm=algo)


if __name__ == '__main__':
  app.run()

