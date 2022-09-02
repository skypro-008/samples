import json


def add_to_json(new_element, path):

    with open(path, "r", encoding='utf-8') as file:
        data = json.load(file)

    data.append(new_element)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file)

