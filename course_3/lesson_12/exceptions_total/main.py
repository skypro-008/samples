
try:
    [1,2,3][4]  # порождает index error
except Exception:
    print("Перехватываем ошибку index error")

try:
    {1:1, 2:2, 3:3 }[4]  # порождает key error
except Exception:
    print("Перехватываем ошибку key error")


try:
    1/0  # порождает division by zero
except Exception:
    print("Перехватываем ошибку деления на ноль")
