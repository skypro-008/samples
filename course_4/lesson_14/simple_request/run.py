import sqlite3

con = sqlite3.connect("netflix.db")
cur = con.cursor()

query = "SELECT * FROM netflix LIMIT 2"

cur.execute(query)
result = cur.fetchall()

print(result)

con.close()
