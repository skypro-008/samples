filename = "data.txt"
f = open(filename, "r")

name = f.readline().strip()
surname = f.readline().strip()
email = f.readline().strip()
phone = f.readline().strip()

print(name)
print(surname)
print(email)
print(phone)
