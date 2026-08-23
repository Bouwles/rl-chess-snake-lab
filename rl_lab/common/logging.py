def format_metric_row(episode: int, score: float, loss: float | None = None) -> dict[str, float | int | None]:
    return {
        "episode": episode,
        "score": score,
        "loss": loss,
    }
