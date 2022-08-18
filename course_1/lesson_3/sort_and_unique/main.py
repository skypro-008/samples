csv = "Вася;39\nПетя;26\nВасилий Петрович;9"


def get_users_list():
    """
    Метод возвращает считанный, сортированный и отфильтрованный список словарей
    """
    data = _read(csv)
    print(data)
    data = _sort(data)

    return _filter(data)


def _read(csv_data):
    """
    Метод считывает данные
    """
    return [x.split(';') for x in csv_data.strip('\\n')]


def _sort(data):
    """
    Метод сортирует данные по возрастанию
    """

    return sorted(data, key=lambda x: int(x[1]))


def _filter(data):
    """
    Метод фильтрует данные
    """
    return [x for x in data if int(x[1]) > 10]


if __name__ == '__main__':
    print(get_users_list())
