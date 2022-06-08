

def print_points(math_points=0, eng_points=0, cs_points=0):

    print(f"Количество баллов за math {math_points}")
    print(f"Количество баллов за eng {eng_points}")
    print(f"Количество баллов за cs {cs_points}")


points_data = {
    "cs_points": 100,
    "eng_points": 75,
    "math_points": 50,
}

print_points(**points_data)


