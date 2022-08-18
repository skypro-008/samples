import sqlite3

con = sqlite3.connect("ladies.db")
cur = con.cursor()

select_query = "SELECT * FROM cats"

cur.execute(query)
result = cur.fetchall()

print(result)

con.close()
