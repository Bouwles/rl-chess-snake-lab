from rl_lab.snake.env import SnakeEnv


def evaluate_policy(policy, episodes: int = 10, size: int = 12, seed: int | None = None) -> dict[str, float]:
    scores: list[int] = []

    for episode in range(episodes):
        env_seed = None if seed is None else seed + episode
        env = SnakeEnv(size=size, seed=env_seed)
        state = env.reset()
        done = False

        while not done:
            action = policy.act(state)
            state, _, done, info = env.step(action)

        scores.append(info["score"])

    return {
        "average_score": sum(scores) / len(scores),
        "best_score": max(scores),
    }
