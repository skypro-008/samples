import sys

def func_test():
    pass

print(sys.getrefcount(func_test))
a = func_test
b = func_test
c = func_test
print(sys.getrefcount(func_test))
