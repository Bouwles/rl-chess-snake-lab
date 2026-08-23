import pytest

chess = pytest.importorskip("chess")

from rl_lab.chess_rl.moves import count_captures, describe_move


def test_describe_move_includes_piece_and_squares():
    board = chess.Board()

    assert describe_move(board, "e2e4") == "white pawn from e2 to e4"


def test_count_captures_counts_capture_moves():
    board = chess.Board()
    moves = ["e2e4", "d7d5", "e4d5"]

    assert count_captures(board, moves) == 1
