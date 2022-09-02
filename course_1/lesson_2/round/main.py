# items = [1.4, -2.11, 3.94, 4.0001, -5.4311, 6.944, -7.2]
#
# # new_items = [item ** 2 for item in items]
#
# # new_items = []
# #
# # for item in items:
# #     new_items.append(item ** 2)
# #
#
# new_items = [item for item in items if item >= 0]
#
# print(new_items)

# У нас есть список слов, нужно выбрать только те слова в которых есть буква автору

words = ["барашек", "ласточка", "журавлик", "кит", "слон"]

# new_items = []
#
# for word in words:
#     if "а" in word:
#         new_items.append(word)
#
# print(new_items)

[print(word) for word in words]


