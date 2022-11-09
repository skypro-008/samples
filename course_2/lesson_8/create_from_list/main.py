ALL_QUESTIONS = [{
    "q": "How many days do we have in a week?",
    "d": "1",
    "a": "7"
}, {
    "q": "How many letters are there in the English alphabet?",
    "d": "3",
    "a": "26"
}, {
    "q": "How many sides are there in a triangle?",
    "d": "2",
    "a": "3"
}, {
    "q": "How many years are there in one Millennium?",
    "d": "2",
    "a": "1000"
}, {
    "q": "How many sides does hexagon have?",
    "d": "4",
    "a": "6"
}]


class Question:

    def __init__(self, question="", answer="", difficulty=0):
        self.question = question
        self.answer = answer
        self.difficulty = difficulty

    def __repr__(self):
        return f"Question({self.question}, {self.answer}, {self.difficulty})"


questions = []

for q_data in ALL_QUESTIONS:
    question = Question(
        question=q_data["q"],
        answer=q_data["a"],
        difficulty=int(q_data["d"])
    )

    questions.append(question)

print(questions)


