import logging


def create_and_set_loggers():

    logger = logging.getLogger("basic")
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler("log.log")
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    file_priority_handler = logging.FileHandler("critical.log")
    file_priority_handler.setLevel(logging.ERROR)
    logger.addHandler(file_priority_handler)



