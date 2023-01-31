import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_random_number(numbers):

    random_number = random.choice(numbers)
    return random_number

counter = 0


for i in range(5):
    random_value = get_random_number(numbers)
    counter += random_value


print(counter)
