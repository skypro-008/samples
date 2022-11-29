import random

WORDS_TO_PLAY = ["code", "bit", "list", "soul", "next"]
MORSE_CODES = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "   "
}


def get_word(words):
    """
    Возвращает случайное слово. Может вернуть с повторами
    :param words: список слов
    :return:
    """
    return random.choice(words)


def get_statistics(answers):
    """
    Возвращает статистику о верных и неверных ответах
    :param answers: список в формате  [True, False, False, True, False]
    :return: словарь с ключами total correct incorrect
    """

    total_count = len(answers)
    correct_count = answers.count(True)
    incorrect_count = answers.count(False)

    return {"total": total_count, "correct": correct_count, "incorrect": incorrect_count}


def print_statistics(stats):
    """
    Выводит статистику о верных и неверных ответах
    :param answers: список в формате  [True, False, False, True, False]
    :return:
    """

    print(f"Всего задачек: {stats['total']}")
    print(f"Отвечено верно: {stats['correct']}")
    print(f"Отвечено неверно: {stats['incorrect']}")


def morse_encode(word, morse_dict):
    """
    Возвращает морзянку на основе слова
    :param word: слово
    :param morse_dict: словарь для кодирования
    :return:
    """
    word_encoded = []
    for letter in word:
        letter_encoded = morse_dict.get(letter, "")
        word_encoded.append(letter_encoded)

    return " ".join(word_encoded)


def main():
    answers = []

    print("Сегодня мы потренируемся расшифровывать морзянку.")
    print("Нажмите Enter и начнем")

    input()

    for i in range(1, 6):

        # - получаем случайное слово с помощью ранее написанной функции
        random_word = get_word(WORDS_TO_PLAY)
        # - кодируем его с помощью ранее написанной функции
        word_morse = morse_encode(random_word, MORSE_CODES)
        # - выводим для пользователя
        print(f"Слово {i} {word_morse}")
        # - получаем ввод
        user_input = input().lower().strip()
        # - сравниваем с загаданным словом
        if user_input == random_word:
            print(f"Верно {random_word}")
            answers.append(True)
        else:
            print(f"Неверно {random_word}")
            answers.append(False)

    stats = get_statistics(answers)
    print_statistics(stats)


main()


