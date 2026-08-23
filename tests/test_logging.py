from rl_lab.common.logging import format_metric_row


def test_format_metric_row_creates_csv_ready_values():
    row = format_metric_row(episode=3, score=8, loss=0.25)

    assert row == {"episode": 3, "score": 8, "loss": 0.25}
