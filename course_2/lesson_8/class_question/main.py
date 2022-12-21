class Question:
    """
    """

    def __init__(self, text, difficulty, correct_answer, is_asked=False, user_answer=""):

        self.text = text
        self.difficulty = difficulty
        self.correct_answer = correct_answer

        self.is_asked = is_asked
        self.user_answer = user_answer
        self.point = self.difficulty * 10

    def set_user_answer(self, answer):
        self.user_answer = answer

    def is_correct(self):
        return self.user_answer == self.correct_answer

    def get_points(self):
        return self.difficulty * 10

    def __repr__(self):
        return f"Question({self.text, self.difficulty, self.correct_answer, self.is_asked, self.user_answer, self.point})"


q_1 = Question("Кто задавал вопрос", 1, "Георгий")
q_1.set_user_answer("Георгий")
print(q_1.is_correct())
print(q_1)
