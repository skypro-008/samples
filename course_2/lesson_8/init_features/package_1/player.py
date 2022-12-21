class Player:

    def __init__(self):
        self.name = ""
        self.score = 0
        self.difficulty = "normal"

    def __repr__(self):
        return f"Player({self.name}, {self.score},{self.difficulty})"
