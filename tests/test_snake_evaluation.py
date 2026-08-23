from rl_lab.snake.baselines import HeuristicSnakePolicy
from rl_lab.snake.evaluate import evaluate_policy


def test_evaluate_policy_returns_average_score():
    result = evaluate_policy(HeuristicSnakePolicy(), episodes=2, size=6, seed=1)

    assert "average_score" in result
    assert "best_score" in result
