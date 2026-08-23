import csv
from pathlib import Path


def format_metric_row(episode: int, score: float, loss: float | None = None) -> dict[str, float | int | None]:
    return {
        "episode": episode,
        "score": score,
        "loss": loss,
    }


def write_metric_rows(path: str | Path, rows: list[dict[str, float | int | None]]) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["episode", "score", "loss"])
        writer.writeheader()
        writer.writerows(rows)
