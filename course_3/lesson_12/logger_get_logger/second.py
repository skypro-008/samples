# Импортируем библиотеку логирования
import logging

# Достаем экземпляр логгера
logger = logging.getLogger("basic")


def function_2():

    # Используем логгер
    logger.debug("Функция function_2 вызвана")

    # Выполняем условно-полезную работу
    print("Функция function_2 что-то делает")
