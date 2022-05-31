# Импортируем библиотеку логирования
import logging


# Функция, которая настраивает логгер "basic"
def create_logger():
    """
    Эта функция создаст и настроит логгер basic
    Функцию нужно импортировать и запустить как можно ближе к началу программы
    Получить этот логгер можно будет в любом файле приложения
    с помощью logger = logging.getLogger("basic")
    """

    # Создаем логгер
    logger = logging.getLogger("basic")
    # Настраиваем его на максимальную чувствительность
    logger.setLevel("DEBUG")

    # Добавляем обработчик – ошибки будут падать в консоль
    console_handler = logging.StreamHandler()
    logger.addHandler(console_handler)

    # Добавляем обработчик – ошибки будут падать в файл
    file_handler = logging.FileHandler("basic.log")
    logger.addHandler(file_handler)

    # Создаем форматтер и настраиваем вывод для обработчиков
    formatter_one = logging.Formatter("%(asctime)s : %(message)s")
    console_handler.setFormatter(formatter_one)
    file_handler.setFormatter(formatter_one)
