from rl_lab.snake.actions import action_name


def test_action_name_labels_snake_actions():
    assert action_name(0) == "turn_left"
    assert action_name(1) == "straight"
    assert action_name(2) == "turn_right"
