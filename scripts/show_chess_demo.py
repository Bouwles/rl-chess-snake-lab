import chess

from rl_lab.chess_rl.demo import run_chess_demo


def main() -> None:
    board = chess.Board()
    print(board)
    for move_uci in run_chess_demo(plies=8):
        board.push(chess.Move.from_uci(move_uci))
        print()
        print(f"Move: {move_uci}")
        print(board)


if __name__ == "__main__":
    main()
