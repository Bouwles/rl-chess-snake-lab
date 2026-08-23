from rl_lab.chess_rl.env import ChessSelfPlayEnv
from rl_lab.chess_rl.train import pick_material_move


def run_chess_demo(plies: int = 12) -> list[str]:
    env = ChessSelfPlayEnv()
    board = env.reset()
    moves: list[str] = []

    for _ in range(plies):
        action = pick_material_move(board, exploration=0.0)
        board, _, done, _ = env.step(action)
        moves.append(action)
        if done:
            break

    return moves


if __name__ == "__main__":
    print(" ".join(run_chess_demo()))
