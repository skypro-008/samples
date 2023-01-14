# Превращаем словарь в аргументы

class DotInSpace:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"DotInSpace({self.x},{self.y},{self.z})"

data = dict(x=20, y=30, z=40)

# coords = DotInSpace(data["x"], data["y"], data["z"])

coords = DotInSpace(**data)

print(coords)
