import json
import os

from number import Number

class NumberManager:

    def __init__(self, path):
        self.path = path
        self.storage = None

        if not os.path.exists(self.path):
            raise FileNotFoundError("Не нашли файл" + self.path)

    def __load(self):

        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        numbers = [Number(value) for value in data]
        return numbers

    def get_all(self):
        all_numbers = self.__load()
        return all_numbers

    def get_even(self):
        all_numbers = self.get_all()
        all_even = [num for num in all_numbers if num.is_even()]
        return all_even

    def get_first(self):
        all_numbers = self.get_all()
        if len(all_numbers) == 0:
            raise ValueError("List of loaded numbers is empty")
        return all_numbers[0]


manager = NumberManager("nums.json")

result = manager.get_even()

print(result)
