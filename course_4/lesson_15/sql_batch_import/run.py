import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

create_table_query = """

DROP TABLE IF EXISTS records;

CREATE TABLE records (
  pk INTEGER PRIMARY KEY AUTOINCREMENT,
  author VARCHAR(255) NOT NULL,
  content VARCHAR(255) NOT NULL
);

"""

cur.executescript(create_table_query)

insert_query = """INSERT INTO records (author, content)  VALUES (?,?)"""

cur.executemany(insert_query, [("Василий", "Люблю базы данных"), ("Рита", "Сегодня прекрасная погода")])

###

fetch_query = """ SELECT * FROM records"""
cur.execute(fetch_query)

print(cur.fetchall())

con.close()
