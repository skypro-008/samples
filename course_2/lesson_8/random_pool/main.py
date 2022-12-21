import random
from enum import unique


class UniqueRandomChoice:

    def __init__(self, pool):
        self.pool = pool
        random.shuffle(self.pool)

    def get(self):
        return self.pool.pop()


unique_source = UniqueRandomChoice([1,2,3,4,5,6,7,8,9,10])

for i in range(10):
    print(unique_source.get())
