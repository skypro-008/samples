import sqlite3

con = sqlite3.connect("source.db")
cur = con.cursor()


query = "SELECT * FROM shop WHERE `cat` = (?)"

cur.execute(query, ("fruit",))

result = cur.fetchall()

print(result)
con.close()
