from rl_lab.common.schedules import decay_epsilon


def test_decay_epsilon_never_goes_below_minimum():
    assert decay_epsilon(0.06, end=0.05, decay=0.5) == 0.05


def test_decay_epsilon_applies_decay_when_above_minimum():
    assert decay_epsilon(1.0, end=0.05, decay=0.9) == 0.9
