import pytest

chess = pytest.importorskip("chess")

from rl_lab.chess_rl.moves import describe_move


def test_describe_move_includes_piece_and_squares():
    board = chess.Board()

    assert describe_move(board, "e2e4") == "white pawn from e2 to e4"
