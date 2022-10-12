import json

import request

# with open("data.json", "r", encoding="utf8") as file:
#     data = json.load(file)
# print(data)

# def load_from_json(path):

#     return data
#
# cats = load_from_json("data.json")
#
# for cat in cats:
#     print(cat["name"])

# LOAD – загрузка из файла
# LOAD S == LOAD FROM STRING – загрузка из строки
#
# DUMP – "сплющивание" в файл
# DUMP S == DUMP TO STRING – "сплющивание" в строку

# file = open("data.json")
# data = json.load(file)
# print(data)

# raw_data = """[{"name": "Luna"}, {"name": "Daisy"}, {"name": "Bell"}]"""
# data = json.loads(raw_data)
# print(data)

data = [{"name": "Luna"}, {"name": "Daisy"}, {"name": "Bell"}]
with open("new.json", "w", encoding="utf-8") as file:
    json.dump(data, file)

# data = [{"name": "Luna"}, {"name": "Daisy"}, {"name": "Bell"}]
# data_json = json.dumps(data)
# print(data_json)
