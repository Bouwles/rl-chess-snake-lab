from rl_lab.common.logging import format_metric_row, write_metric_rows


def test_format_metric_row_creates_csv_ready_values():
    row = format_metric_row(episode=3, score=8, loss=0.25)

    assert row == {"episode": 3, "score": 8, "loss": 0.25}


def test_write_metric_rows_writes_csv(tmp_path):
    output = tmp_path / "metrics.csv"
    rows = [format_metric_row(episode=1, score=2, loss=0.5)]

    write_metric_rows(output, rows)

    assert output.read_text(encoding="utf-8") == "episode,score,loss\n1,2,0.5\n"
