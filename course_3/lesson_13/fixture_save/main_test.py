import json

from main import add_to_json

def test_add_to_json_basic(new_data):

    path = "data.json"
    add_to_json(new_data, path)

    with open(path, encoding='utf-8') as file:
        full_data = json.load(file)
    last_element = full_data[-1]

    # Проверяем, что полученные данные соответствуют полученным из фикстуры
    assert last_element == new_data
