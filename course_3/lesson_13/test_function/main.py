def get_grade_verbose(grade):
    """ Возвращает оценку на естественном языке"""

    if grade == 2:
        return "Плохо"
    elif grade == 3:
        return "Удовлетворительно"
    elif grade == 4:
        return "Хорошо"
    elif grade == 5:
        return "Отлично"

    raise ValueError("Unexpected Value, 2-5 expected")


def get_period(hour):

    if type(hour) != int:
        raise TypeError("int expected")

    if hour < 0 or hour > 24:
        raise ValueError("0-24 expected")

    """ принимает целочисленный час суток 0-24 и возвращает время суток"""

    if hour in range(0,7):
      return "ночь"
    if hour in range(7,12):
      return "утро"
    if hour in range(12,18):
      return "день"
    if hour in range(18,25):
      return "вечер"

