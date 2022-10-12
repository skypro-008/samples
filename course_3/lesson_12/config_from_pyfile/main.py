from flask import Flask
app = Flask(__name__)

# переносим все переменные из файла в суперсловарь конфигов
app.config.from_pyfile("config.py")

# пробуем достать из суперсловаря нужное
print(app.config.get("MYCONFIG"))

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)

