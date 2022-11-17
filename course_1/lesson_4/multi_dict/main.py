words_easy = {
    "family":"семья",
    "hand": "рука",
    "people":"люди",
    "evening": "вечер",
    "minute":"минута",
}

words_medium = {
    "believe":"верить",
    "feel": "чувствовать",
    "make":"делать",
    "open": "открывать",
    "think":"думать",
}

words_hard = {
    "rural":"деревенский",
    "fortune": "удача",
    "exercise":"упражнение",
    "suggest": "предлагать",
    "except":"кроме",
}

dicts_by_difficulty = {
    "easy": words_easy,
    "medium": words_medium,
    "hard": words_hard,
}

while True:
    user_input = input()
    if user_input in dicts_by_difficulty:
        words_top_play = dicts_by_difficulty[user_input]
        break
    else:
        print('повторите ввод')

print(words_top_play)

