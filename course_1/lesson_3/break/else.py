import random

eng_words = ['code', 'bit', 'list', 'soul', 'next']
morse_code = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
              'i': '••',
              'j': '•———', 'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•', 'o': '———', 'p': '•——•', 'q': '——•—',
              'r': '•—•',
              's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—', 'y': '—•——', 'z': '——••'}
answers = []


def morse_encode(word):
    new_word = ""
    for symbol in word:
        new_word += morse_code[symbol]
        return new_word


def get_word():
    word = random.choice(eng_words)

    return word


def print_statistics(*answers):
    correct_answers = 0
    incorrect_answers = 0
    for correct in answers:
        if correct == True:
            correct_answers += 1
    return correct_answers
    for incorrect in answers:
        if incorrect == False:
            incorrect_answers += 1
    return incorrect_answers


print('Сегодня мы потренируемся расшифровывать морзянку')
input('Нажмите Enter и начнем ')

for correct in range(len(eng_words)):
    word = get_word()
    user_answers = input(f'Слово {correct + 1} : {morse_encode(word)} На английском языке: ')
    if user_answers == word:
        print(f'Верно, это {word}')
        answers.append(True)
    else:
        print(f'Неверно, это {word}')
        answers.append(False)


print_statistics(answers)
