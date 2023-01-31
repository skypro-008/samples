class Product:

    def __init__(self, icon="", name="", katigory="", kcal=0):
        self.icon = icon
        self.name = name
        self.katigory = katigory
        self.kcal = kcal

    def get_category(self):
        return self.katigory.lower()

    def get_katigory(self):
        return self.get_category()


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


