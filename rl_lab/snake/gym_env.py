import numpy as np
from gymnasium import Env, spaces

from rl_lab.snake.env import SnakeEnv


class SnakeGymEnv(Env):
    metadata = {"render_modes": []}

    def __init__(self, size: int = 12, seed: int | None = None):
        super().__init__()
        self.env = SnakeEnv(size=size, seed=seed)
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(low=0, high=1, shape=(11,), dtype=np.float32)

    def reset(self, *, seed: int | None = None, options: dict | None = None):
        super().reset(seed=seed)
        if seed is not None:
            self.env = SnakeEnv(size=self.env.size, seed=seed)
        observation = np.array(self.env.reset(), dtype=np.float32)
        return observation, {"score": self.env.score}

    def step(self, action: int):
        state, reward, done, info = self.env.step(int(action))
        observation = np.array(state, dtype=np.float32)
        return observation, float(reward), bool(done), False, info
