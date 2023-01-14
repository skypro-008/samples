# 🍏	Аpple	fruit	45
# 🍎	Apple	fruit	49
# 🍌	Banana	fruit	95
# 🥑	Avocado	fruit	160
# 🍅	Tomato	veggie	20
# 🥦	Broccoli	veggie	34
# 🥕	Carrot	veggie	100
# 🍪	Cookie	sweets	514
# 🍩	Donut	sweets	300
# 🍰	Cake	sweets	400

class Product:

    def __init__(self, icon="", name="", cat="", kcal=0):
        self.icon = icon
        self.name = name
        self.cat = cat
        self.kcal = kcal

    def __repr__(self):
        return f"Product(" \
               f"{self.icon}," \
               f"{self.name}," \
               f"{self.cat}," \
               f"{self.kcal}" \
               f")"


products_data = [

    {
        "icon": "🍏",
        "name": "Аpple Green",
        "cat": "fruit",
        "kcal": 45,
    },
    {
        "icon": "🍎",
        "name": "Аpple Red",
        "cat": "fruit",
        "kcal": 45,
    },
    {
        "icon": "🥦",
        "name": "Broccoli",
        "cat": "veggie",
        "kcal": 45,
    }
]


def create_products_from_data(data):
    """
    Возвращает список экз класса Product из списка словарей
    :param data: список словарецй с ключами icon name cat kcal
    :return:
    """

    products = []

    for p_data in data:
        product = Product(
            icon=p_data["icon"], name=p_data["name"], cat=p_data["cat"], kcal=p_data["kcal"]
        )

        products.append(product)

    return products


result = create_products_from_data(products_data)

print(result)
#
# def create_instances_from_dict(data_dict):
#
#     # заводим список с продуктами
#     products = []
#
#     for product_data in data_dict:
#         # создаем экземпляр продукта
#         product_instance = Product(
#             product_data["icon"],
#             product_data["name"],
#             product_data["cat"],
#             product_data["kcal"]
#         )
#         # добавляем экземпляр продукта в список
#         products.append(product_instance)
#
#     # возвращаем в список
#     return products
#
# # тестируем
# products_in_list = create_instances_from_dict(products_data)
# print(products_in_list)
#
# #
# products = [
#     Product("🍏", "Аpple Green", "fruit", 45),
#     Product("🍎", "Аpple Red", "fruit", 45),
#     Product("🍌", "Banana", "fruit", 45),
#     Product("🥑", "Avocado", "fruit", 45),
#     Product("🍅", "Tomato", "veggie", 45),
#     Product("🥦", "Broccoli", "veggie", 45),
#     Product("🥕", "Carrot", "veggie", 45),
#     Product("🍪", "Cookie", "sweets", 45),
#     Product("🍩", "Donut", "sweets", 45),
#     Product("🍰", "Cake", "sweets", 45),
# ]
#
# print(products)
