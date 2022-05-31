# Импортируем библиотеку логирования
import logging

# Импортируем функцию создания логгера
from loggers import create_logger

from first import function_1
from second import function_2

# Запускаем настройку логгера, настроенный логгер НЕ импортируем!
create_logger()

# Достаем экземпляр логгера
logger = logging.getLogger("basic")

# Используем логгер
logger.info("Приложение запускается")

# Вызываем функции, у которых есть свои логгеры
function_1()
function_2()

# Используем логгер
logger.info("Приложение завершается")
