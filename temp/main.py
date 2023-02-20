# Напишите декоратор off,
# который при вызове функции
# будет вместо функции выводить
# в консоль "функция отключена"

# TODO напишите декратор off здесь
def off(function):
    def wrapper():
        print("функция отключена")
    return wrapper

@off
def func():
    print("работаю")

if __name__=="__main__":
    func()
