import sqlite3

con = sqlite3.connect("netflix.db")
cur = con.cursor()

query = "SELECT title, country, release_year, listed_in, description FROM netflix ORDER by release_year DESC LIMIT 1 "

cur.execute(query)
result = cur.fetchall()
the_movie = result[0]

keys = ["title", "country", "release_year", "listed_in", "description"]

the_movie_dict = dict(zip(keys, the_movie))

print(the_movie_dict)

con.close()
