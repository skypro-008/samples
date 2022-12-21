def avg_from_line(line):

    numbers = line.split(" ")

    numbers_as_ints = [int(num) for num in numbers]

    total = sum(numbers_as_ints)
    number_count = len(numbers_as_ints)

    avg = total / number_count

    return avg
