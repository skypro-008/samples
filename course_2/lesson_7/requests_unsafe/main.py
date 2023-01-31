import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
result = requests.get("https://jsonkeeper.com/b/OTF8", verify = False)

data = result.json()

print(data)

