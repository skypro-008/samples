# print(__name__)
#
#
# # __name__ – имя модуля (файла) если модуль импортирован
# # __name__ – __main__ если модуль запущен напрямую

def foo():
    print("foo")
    print("foo")
    print("foo")

if __name__ == "__main__":
    foo()
