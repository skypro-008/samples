class Product:

    def __init__(self, icon="", name="", cat="", kcal=0):
        self.icon = icon
        self.name = name
        self.cat = cat
        self.kcal = kcal



    def dict(self) -> dict:
        result = {
            "name": self.name.title(),
            "cat": self.cat.lower(),
            "kcal": self.kcal,
        }

        return result

    def __repr__(self):
        return f"Product(" \
               f"{self.icon}," \
               f"{self.name}," \
               f"{self.cat}," \
               f"{self.kcal}" \
               f")"


products = []

products.append(Product("🍏", "Аpple", "fruit", 45))
products.append(Product("🍎", "Apple", "fruit", 49))
products.append(Product("🍅", "Tomato", "veggie", 20))
products.append(Product("🍩", "Donut", "sweets", 300))


def get_fruits_from_products(products):

    # fruits = []
    # for product in products:
    #     if product.cat == "fruit":
    #         fruits.append(product)
    #
    # return fruits

    return [product for product in products if product.cat == "fruit"]


fruits_found = get_fruits_from_products(products)
print(fruits_found)
