import requests as requests

source_url = "https://jsonkeeper.com/b/O8MV"
result = requests.get(source_url)
words = result.json()

# Дальше можно работать со словами

word = words[0]

print(word)
