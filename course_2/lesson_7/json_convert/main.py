import json

data = {

    2: True,
    3: False,
    4: 'Nice',
}

data_in_json = json.dumps(data)

print(data_in_json)
