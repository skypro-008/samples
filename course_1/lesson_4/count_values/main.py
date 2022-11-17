answers = {
    "first": True,
    "second": False,
    "third": True,
    "fourth": False,
    "fifth": False,
    "sixth": False
}

correct = []
incorrect = []

for answer, is_correct in answers.items():
    if is_correct:
        correct.append(answer)
    else:
        incorrect.append(answer)

print(correct)
print(incorrect)

