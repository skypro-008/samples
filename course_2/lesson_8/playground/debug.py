print("Введите разделенные пробелом числа, например 3 6 12 4 9 5")

line = input() # "1 3 4 5 7"

numbers = line.split(" ")

numbers_as_ints = [int(num) for num in numbers]

total = sum(numbers)
number_count = len(numbers_as_ints)

avg = total / number_count

print(avg)
