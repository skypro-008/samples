import sqlite3

con = sqlite3.connect("sample.db")
cur = con.cursor()



result = cur.fetchall()

print(result)
con.close()
