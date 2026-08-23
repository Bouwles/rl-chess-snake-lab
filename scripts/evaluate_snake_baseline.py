from rl_lab.snake.baselines import HeuristicSnakePolicy, RandomSnakePolicy
from rl_lab.snake.evaluate import evaluate_policy


def main() -> None:
    random_result = evaluate_policy(RandomSnakePolicy(seed=1), episodes=5, seed=1)
    heuristic_result = evaluate_policy(HeuristicSnakePolicy(), episodes=5, seed=1)

    print(f"Random baseline: {random_result}")
    print(f"Heuristic baseline: {heuristic_result}")


if __name__ == "__main__":
    main()
