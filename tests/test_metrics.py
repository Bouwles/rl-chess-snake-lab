from rl_lab.common.metrics import moving_average


def test_moving_average_uses_requested_window():
    assert moving_average([1, 2, 3, 4], window=2) == [1.0, 1.5, 2.5, 3.5]
