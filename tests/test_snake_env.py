from rl_lab.snake.env import Direction, SnakeEnv


def test_snake_reset_returns_fixed_size_state():
    env = SnakeEnv(size=8, seed=1)

    state = env.reset()

    assert len(state) == 11
    assert env.score == 0


def test_snake_eating_food_increases_score():
    env = SnakeEnv(size=8, seed=1)
    env.reset()
    head_x, head_y = env.snake[0]
    env.direction = Direction.RIGHT
    env.food = (head_x + 1, head_y)

    _, reward, done, info = env.step(1)

    assert reward == 10.0
    assert done is False
    assert info["score"] == 1


def test_snake_wall_collision_ends_episode():
    env = SnakeEnv(size=6, seed=1)
    env.reset()
    env.snake = [(0, 2)]
    env.direction = Direction.LEFT

    _, reward, done, _ = env.step(1)

    assert reward == -10.0
    assert done is True


def test_snake_episode_can_end_after_too_many_steps():
    env = SnakeEnv(size=4, seed=1)
    env.reset()
    env.steps = env.size * env.size * 2

    _, _, done, _ = env.step(1)

    assert done is True
