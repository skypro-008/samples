import os
import dotenv
from flask import Flask

app = Flask(__name__)

# загружаем в переменные окружения данные из файла .env
dotenv.load_dotenv(override=True)

# В зависимости от значения APP_CONFIG подключаем тот или другой конфиг
if os.environ.get("APP_CONFIG") == "development":
    app.config.from_pyfile('config/development.py')
else:
    app.config.from_pyfile('config/production.py')

# Выводим получившийся конфиг
print(app.config.get("MY_VALUE"))
