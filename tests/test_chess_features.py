import pytest

chess = pytest.importorskip("chess")

from rl_lab.chess_rl.features import board_to_tensor, material_label, material_score


def test_board_to_tensor_has_piece_planes():
    board = chess.Board()

    tensor = board_to_tensor(board)

    assert tensor.shape == (12, 8, 8)
    assert tensor.sum() == 32


def test_material_score_starts_equal():
    board = chess.Board()

    assert material_score(board) == 0


def test_material_label_reports_equal_position():
    board = chess.Board()

    assert material_label(board) == "material equal"
