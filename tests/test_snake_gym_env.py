from rl_lab.snake.gym_env import SnakeGymEnv


def test_snake_gym_env_reset_returns_observation_and_info():
    env = SnakeGymEnv(size=8, seed=1)

    observation, info = env.reset(seed=1)

    assert observation.shape == (11,)
    assert info["score"] == 0


def test_snake_gym_env_step_uses_gymnasium_api():
    env = SnakeGymEnv(size=8, seed=1)
    env.reset(seed=1)

    observation, reward, terminated, truncated, info = env.step(1)

    assert observation.shape == (11,)
    assert isinstance(reward, float)
    assert isinstance(terminated, bool)
    assert truncated is False
    assert "score" in info
