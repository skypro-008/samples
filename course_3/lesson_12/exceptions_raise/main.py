# Несколько примеров того, как создаются функции, вызывающие ошибки


def func_with_value_error(value):
    """
    Функция для демонстрации вызова ошибки
    Падаетс с ошибкой если значение неположительное
    """
    if value <= 0:
        raise ValueError("expected value to be positive")


# func_with_value_error(1) # сработает как надо
# func_with_value_error(0) # выбросит ошибку

def func_with_type_error(value):
    """
    Функция для демонстрации вызова ошибки
    Падает с ошибкой если значение неположительное
    """
    if type(value) != int:
        raise TypeError("expected value to be an int")

# func_with_type_error(1) # сработает как надо
# func_with_type_error("1") # выбросит ошибку

