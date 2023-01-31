class Number:

    def __init__(self, value):

        if type(value) != int:
            raise ValueError

        self.value = value

    def __repr__(self):
        return f"Number({self.value})"

    def is_even(self):
        """
        Возвращает, является ли число четным
        :return:
        """
        return self.value % 2 == 0

    def is_odd(self):
        """
        Возврашает, является ли числор нечетным
        :return:
        """
        return not self.is_even()
