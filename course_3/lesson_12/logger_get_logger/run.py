from flask import Flask, render_template
app = Flask(__name__)

# Импортируем библиотеку логирования
import logging

# Импортируем функцию создания логгера
from loggers import create_logger

from first import function_1
from second import function_2

# Запускаем настройку логгера, настроенный логгер НЕ импортируем!
create_logger()

# Достаем экземпляр логгера
logger = logging.getLogger("basic")

# Используем логгер
logger.info("Приложение запускается")

# Вызываем функции, у которых есть свои логгеры
function_1()
function_2()

# Используем логгер
logger.info("Приложение завершается")


@app.route('/')
def index():
    return "it works"

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)


