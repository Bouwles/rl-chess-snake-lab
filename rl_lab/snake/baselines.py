import random


class RandomSnakePolicy:
    def __init__(self, seed: int | None = None):
        self.random = random.Random(seed)

    def act(self, state: list[int]) -> int:
        return self.random.randrange(3)
