import json


def _load():
    """
    Загружает данные из файла
    """
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_all():
    """
    Возввращает полный список кандидатов
    """
    return _load()


def get_by_pk(pk):
    """
    Возвращает одну запись по ее pk
    """
    items = _load()
    for item in items:
        if item["pk"] == pk:
            return item
