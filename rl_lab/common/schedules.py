def decay_epsilon(current: float, end: float, decay: float) -> float:
    return max(end, current * decay)
