import pytest

chess = pytest.importorskip("chess")

from rl_lab.chess_rl.rendering import piece_family


def test_piece_family_uses_piece_type_names_instead_of_letters():
    assert piece_family(chess.Piece(chess.KING, chess.WHITE)) == "king"
    assert piece_family(chess.Piece(chess.PAWN, chess.BLACK)) == "pawn"
