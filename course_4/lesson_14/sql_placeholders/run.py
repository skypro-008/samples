import sqlite3

con = sqlite3.connect("sample.db")
cur = con.cursor()

query = "SELECT * FROM sample WHERE  `value` LIKE :substring_pattern "
substring = "ошки"
cur.execute(query, {"substring_pattern": f"%{substring}%"})

result = cur.fetchall()

print(result)
con.close()

