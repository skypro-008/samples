class Product:

    def __init__(self, icon="", name="", katigory="", kcal=0):
        self.icon = icon
        self.name = name
        self.katigory = katigory
        self.kcal = kcal

    def get_category(self):
        return self.katigory.lower()

    def set_category(self, new_category):

        self.katigory = new_category.lower().strip()

    def __repr__(self):
        return f"Product(" \
               f"{self.icon}," \
               f"{self.name}," \
               f"{self.get_category()},"
               f"{self.kcal}" \
               f")"


product = Product("🍏", "Аpple", "fruit", 45)

print(product.get_category())

product.set_category("Sweets  ")

print(product)

