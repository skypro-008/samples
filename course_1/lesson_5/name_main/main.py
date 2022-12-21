def avg_from_line(line):
    """
    Из строки с числами разделенными пробелом
    Получает среднее арифметическое этих чисел
    :param line:
    :return:
    """
    numbers = line.split(" ")

    numbers_as_ints = [int(num) for num in numbers]

    total = sum(numbers_as_ints)
    number_count = len(numbers_as_ints)

    avg = total / number_count

    return avg


def main():
    print("Введите числа через пробел")
    user_input = input()

    result = avg_from_line(user_input)

    print(result)


if __name__ == "__main__":
    print("meow")
    main()

