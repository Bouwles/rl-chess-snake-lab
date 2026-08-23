import random
from collections import deque
from typing import Any


class ReplayMemory:
    def __init__(self, capacity: int, seed: int | None = None):
        self.buffer: deque[Any] = deque(maxlen=capacity)
        self.random = random.Random(seed)

    def push(self, experience: Any) -> None:
        self.buffer.append(experience)

    def sample(self, batch_size: int) -> list[Any]:
        return self.random.sample(list(self.buffer), batch_size)

    def __len__(self) -> int:
        return len(self.buffer)
