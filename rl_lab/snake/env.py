from __future__ import annotations

import random
from enum import Enum


class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)


TURN_RIGHT = {
    Direction.UP: Direction.RIGHT,
    Direction.RIGHT: Direction.DOWN,
    Direction.DOWN: Direction.LEFT,
    Direction.LEFT: Direction.UP,
}

TURN_LEFT = {value: key for key, value in TURN_RIGHT.items()}


class SnakeEnv:
    """Small Gym-style Snake environment with a compact 11-value state."""

    def __init__(self, size: int = 12, seed: int | None = None):
        self.size = size
        self.random = random.Random(seed)
        self.snake: list[tuple[int, int]] = []
        self.direction = Direction.RIGHT
        self.food = (0, 0)
        self.score = 0
        self.steps = 0
        self.reset()

    def reset(self) -> list[int]:
        center = self.size // 2
        self.snake = [(center, center), (center - 1, center), (center - 2, center)]
        self.direction = Direction.RIGHT
        self.score = 0
        self.steps = 0
        self._place_food()
        return self._state()

    def step(self, action: int) -> tuple[list[int], float, bool, dict[str, int]]:
        if action == 0:
            self.direction = TURN_LEFT[self.direction]
        elif action == 2:
            self.direction = TURN_RIGHT[self.direction]

        dx, dy = self.direction.value
        head_x, head_y = self.snake[0]
        new_head = (head_x + dx, head_y + dy)
        self.steps += 1

        if self._is_collision(new_head):
            return self._state(), -10.0, True, {"score": self.score}

        self.snake.insert(0, new_head)
        reward = -0.01
        if new_head == self.food:
            self.score += 1
            reward = 10.0
            self._place_food()
        else:
            self.snake.pop()

        too_long_without_food = self.steps > self.size * self.size * 2
        return self._state(), reward, too_long_without_food, {"score": self.score}

    def _place_food(self) -> None:
        open_cells = [
            (x, y)
            for y in range(self.size)
            for x in range(self.size)
            if (x, y) not in self.snake
        ]
        self.food = self.random.choice(open_cells)

    def _is_collision(self, point: tuple[int, int]) -> bool:
        x, y = point
        return (
            x < 0
            or x >= self.size
            or y < 0
            or y >= self.size
            or point in self.snake
        )

    def _danger(self, direction: Direction) -> int:
        head_x, head_y = self.snake[0]
        dx, dy = direction.value
        return int(self._is_collision((head_x + dx, head_y + dy)))

    def _state(self) -> list[int]:
        left = TURN_LEFT[self.direction]
        right = TURN_RIGHT[self.direction]
        food_x, food_y = self.food
        head_x, head_y = self.snake[0]

        return [
            self._danger(left),
            self._danger(self.direction),
            self._danger(right),
            int(self.direction == Direction.LEFT),
            int(self.direction == Direction.RIGHT),
            int(self.direction == Direction.UP),
            int(self.direction == Direction.DOWN),
            int(food_x < head_x),
            int(food_x > head_x),
            int(food_y < head_y),
            int(food_y > head_y),
        ]
