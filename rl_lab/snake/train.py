import random
from dataclasses import dataclass

import torch
from torch import nn, optim

from rl_lab.common.dqn import DQN
from rl_lab.common.replay import ReplayMemory
from rl_lab.snake.env import SnakeEnv


@dataclass
class SnakeTrainingConfig:
    episodes: int = 100
    gamma: float = 0.9
    epsilon_start: float = 1.0
    epsilon_end: float = 0.05
    epsilon_decay: float = 0.98
    batch_size: int = 64
    learning_rate: float = 0.001


def choose_action(model: DQN, state: list[int], epsilon: float) -> int:
    if random.random() < epsilon:
        return random.randrange(3)
    with torch.no_grad():
        q_values = model(torch.tensor([state], dtype=torch.float32))
        return int(torch.argmax(q_values).item())


def train_snake(config: SnakeTrainingConfig = SnakeTrainingConfig()) -> DQN:
    env = SnakeEnv()
    model = DQN(input_size=11, output_size=3)
    optimizer = optim.Adam(model.parameters(), lr=config.learning_rate)
    loss_fn = nn.MSELoss()
    memory = ReplayMemory(capacity=10_000)
    epsilon = config.epsilon_start

    for _ in range(config.episodes):
        state = env.reset()
        done = False
        while not done:
            action = choose_action(model, state, epsilon)
            next_state, reward, done, _ = env.step(action)
            memory.push((state, action, reward, next_state, done))
            state = next_state

            if len(memory) < config.batch_size:
                continue

            batch = memory.sample(config.batch_size)
            states, actions, rewards, next_states, dones = zip(*batch)
            states_t = torch.tensor(states, dtype=torch.float32)
            actions_t = torch.tensor(actions).unsqueeze(1)
            rewards_t = torch.tensor(rewards, dtype=torch.float32)
            next_states_t = torch.tensor(next_states, dtype=torch.float32)
            dones_t = torch.tensor(dones, dtype=torch.bool)

            q_values = model(states_t).gather(1, actions_t).squeeze()
            next_q_values = model(next_states_t).max(1).values.detach()
            targets = rewards_t + config.gamma * next_q_values * (~dones_t)

            loss = loss_fn(q_values, targets)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        epsilon = max(config.epsilon_end, epsilon * config.epsilon_decay)

    return model


if __name__ == "__main__":
    torch.save(train_snake().state_dict(), "snake_dqn.pt")
