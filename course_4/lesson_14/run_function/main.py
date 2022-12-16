import sqlite3

DBPATH = "netflix.db"


def run_query_and_fetch(query, db_path):
    """
    Запускает запрос, возвращает список кортежей
    :param cursor: ссылка на курсор
    :param query: текст запроса
    :return:
    """
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    con.close()
    return result


query = "SELECT title FROM netflix LIMIT 5"
result = run_query_and_fetch(query, DBPATH)

print(result)


