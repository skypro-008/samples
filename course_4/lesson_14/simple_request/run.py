import sqlite3

con = sqlite3.connect("netflix.db")
cur = con.cursor()

query = "SELECT title FROM netflix LIMIT 1"

cur.execute(query)
result = cur.fetchall()

print(result)

con.close()
