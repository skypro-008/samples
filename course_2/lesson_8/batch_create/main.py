class Product:
    """

    """

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


def create_instances_from_dict(data_dict):

    products = [Product(**product_data) for product_data in data_dict]
    return products

create_instances_from_dict(products_data)



#
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
