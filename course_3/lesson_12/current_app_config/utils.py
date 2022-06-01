# Импортируем из фласка ссылку на текущий экземпляр приложения
from flask import current_app


def foo():
    """ Функция возвращает приветствие из настроек """
    greeting = current_app.config.get("GREETING")
    return greeting

