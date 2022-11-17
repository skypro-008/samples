from pprint import pprint as pp
import sqlite3

con = sqlite3.connect("netflix.db")
cur = con.cursor()

# Выполняем запрос
query = "SELECT * FROM netflix LIMIT 5"
cur.execute(query)
result_all = cur.fetchall()

# Перечисляем ключи, которые нам понадобятся
keys = [
    "show_id",
    "type",
    "title",
    "director",
    "cast",
    "country",
    "date_added",
    "release_year",
    "rating",
    "duration",
    "duration_type",
    "listed_in",
    "description"
]


# Превращаем список безымянных кортежей в список словарей
result = []

# Перебираем все полученные записи
for result_row in result_all:

    # Ключ словаря – очередной ключ, значение, очередное значение кортежа
    result.append(
        {keys[i]: result_row[i] for i in range(len(keys))}
    )

pp(result)



