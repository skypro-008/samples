# Импортируем библиотеку логирования
import logging

# Достаем экземпляр логгера
logger = logging.getLogger("basic")


def function_1():

    # Используем логгер
    logger.debug("Функция function_1 вызвана")

    # Выполняем условно-полезную работу
    print("Функция function_1 что-то делает")
