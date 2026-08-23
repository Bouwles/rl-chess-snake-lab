import random


class RandomSnakePolicy:
    def __init__(self, seed: int | None = None):
        self.random = random.Random(seed)

    def act(self, state: list[int]) -> int:
        return self.random.randrange(3)


class HeuristicSnakePolicy:
    """Avoid immediate danger, then prefer moving straight."""

    def act(self, state: list[int]) -> int:
        danger_left, danger_straight, danger_right = state[:3]
        if not danger_straight:
            return 1
        if not danger_left:
            return 0
        if not danger_right:
            return 2
        return 1
