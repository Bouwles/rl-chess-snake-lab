ACTION_NAMES = {
    0: "turn_left",
    1: "straight",
    2: "turn_right",
}


def action_name(action: int) -> str:
    return ACTION_NAMES[action]
