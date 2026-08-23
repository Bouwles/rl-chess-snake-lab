def moving_average(values: list[float], window: int) -> list[float]:
    averages: list[float] = []
    for index in range(len(values)):
        start = max(0, index - window + 1)
        visible = values[start : index + 1]
        averages.append(sum(visible) / len(visible))
    return averages
