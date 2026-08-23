import chess

from rl_lab.chess_rl.rendering import piece_family


def describe_move(board: chess.Board, move_uci: str) -> str:
    move = chess.Move.from_uci(move_uci)
    piece = board.piece_at(move.from_square)
    if piece is None:
        raise ValueError(f"No piece on {chess.square_name(move.from_square)}")

    color = "white" if piece.color == chess.WHITE else "black"
    return (
        f"{color} {piece_family(piece)} from "
        f"{chess.square_name(move.from_square)} to {chess.square_name(move.to_square)}"
    )


def count_captures(board: chess.Board, move_uci_list: list[str]) -> int:
    board = board.copy()
    captures = 0
    for move_uci in move_uci_list:
        move = chess.Move.from_uci(move_uci)
        if board.is_capture(move):
            captures += 1
        board.push(move)
    return captures
