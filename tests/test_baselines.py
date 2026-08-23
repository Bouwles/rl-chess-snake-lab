from rl_lab.snake.baselines import HeuristicSnakePolicy, RandomSnakePolicy


def test_random_snake_policy_returns_valid_action():
    policy = RandomSnakePolicy(seed=1)

    action = policy.act([0] * 11)

    assert action in {0, 1, 2}


def test_heuristic_snake_policy_avoids_straight_danger():
    policy = HeuristicSnakePolicy()
    state = [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0]

    assert policy.act(state) != 1
