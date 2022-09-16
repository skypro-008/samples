class Word:

    def __init__(self, sub_words):
        self.sub_words = sub_words

    def has_sub_word(self, attempt):
        """
        Возврашает , находится ли слово с списке подслов
        """

        return attempt.strip().lower() in self.sub_words



# создаем экземпляр
sub_words = ["кря", "бря", "мря"]
basic_word = Word(sub_words)

# используем метод
print(basic_word.has_sub_word("бря"))
print(basic_word.has_sub_word("Бря"))
print(basic_word.has_sub_word("Бря "))
print(basic_word.has_sub_word("уря"))
print(basic_word.has_sub_word("зря"))

