from rl_lab.snake.baselines import RandomSnakePolicy


def test_random_snake_policy_returns_valid_action():
    policy = RandomSnakePolicy(seed=1)

    action = policy.act([0] * 11)

    assert action in {0, 1, 2}
