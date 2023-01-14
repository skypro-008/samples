import requests

result = requests.get("https://www.jsonkeeper.com/b/OTF8", verify = False)

data = result.json()

print(data)

