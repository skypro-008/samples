import sqlite3


def get_connection(path):
    """ Возвращаем соединение с базой"""
    connection = sqlite3.connect(path, check_same_thread=False)
    return connection


connection = get_connection("source.db")
