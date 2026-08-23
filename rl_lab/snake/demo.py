from rl_lab.snake.env import SnakeEnv


def run_random_snake_demo(steps: int = 30) -> list[tuple[int, int]]:
    env = SnakeEnv(size=10, seed=7)
    env.reset()
    path = [env.snake[0]]
    for step in range(steps):
        _, _, done, _ = env.step(step % 3)
        path.append(env.snake[0])
        if done:
            break
    return path


if __name__ == "__main__":
    print(run_random_snake_demo())
