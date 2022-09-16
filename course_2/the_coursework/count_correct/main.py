class Question:

    def __init__(self, answer, correct_answer):
        self.answer = answer
        self.correct_answer = correct_answer

    def is_correct(self):
        return self.answer == self.correct_answer


words = [
    Question("one", "one"),
    Question("two", "one"),
    Question("one", "two"),
    Question("two", "two")
]

correct_count = 0

for word in words:
    if word.is_correct():
        correct_count += 1

print(correct_count)


