class Player:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def set_values(self, name, score):
        self.name = name
        self.score = score

    def __call__(self):
        print("не надо меня звать")

    def __int__(self):
        return self.score

    def __repr__(self):
        return f"Player({self.name}, {self.score})"



player = Player("Денис",100)

print(int(player)*2)

# player.set_values()
# print(player)
#
#
# player = Player()
# player.set_values()
# print(player)

