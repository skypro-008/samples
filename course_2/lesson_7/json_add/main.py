import json


def read_from_json(filename):
    """ читает данные из JSON строки и возврашает в виде списка словарей"""
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def save_to_json(filename, data):
    """ сохраняет данные из списка словарей в JSON строку"""
    with open(filename, "w", encoding="utf-8") as file:
        data = json.dump(data, file)
    return data


def add_to_json(filename, new_element):
    """добавляет элемент в список, используя две вышеупомянутые функции"""
    data = read_from_json(filename)
    data.append(new_element)
    save_to_json(filename, data)

# А теперь небольшой пример с добавлением кота в список километров

filename = "cats.json"

print("Введите кличку кота")
user_input = input()

new_cat = {"name": user_input}
add_to_json(filename, new_cat)

print("Кот добавлен")


