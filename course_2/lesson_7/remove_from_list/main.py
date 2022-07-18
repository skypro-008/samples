

# Удалить что то с pk =2

# Способ 1

items = [ {"pk": 1, "data": 11},  {"pk": 2, "data": 12},  {"pk": 3, "data": 13}, ]

for index, item in enumerate(items):
    if item["pk"] == 2:
        del items[index]

print(items)

# Способ 2

items = [ {"pk": 1, "data": 11},  {"pk": 2, "data": 12},  {"pk": 3, "data": 13}, ]

for index, item in enumerate(items):
    if item["pk"] == 2:
        items.remove((item))

print(items)

# Способ 3

items = [ {"pk": 1, "data": 11},  {"pk": 2, "data": 12},  {"pk": 3, "data": 13}, ]

items = [item for item in items if item["pk"] != 2]

print(items)
