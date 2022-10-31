import os

import dotenv
from flask import Flask

app = Flask(__name__)

# Загружаем переменные окружения из ближайшего .env файла
dotenv.load_dotenv(override=True)

# В зависимости от значения APP_CONFIG подключаем тот или другой конфиг

if os.environ.get("APP_CONFIG") == "development":
    app.config.from_pyfile('config/development.py')
else:
    app.config.from_pyfile('config/production.py')

# пробуем достать из суперсловаря настроек нужное
print(app.config.get("MY_VALUE"))

