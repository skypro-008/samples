import sqlite3

con = sqlite3.connect("source.db")
cur = con.cursor()

category = "fruit"
query = "SELECT * FROM shop WHERE `cat` = (?)"
cur.execute(query, (category,))

result = cur.fetchall()

print(result)
con.close()
