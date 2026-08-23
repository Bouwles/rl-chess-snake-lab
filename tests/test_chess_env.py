import pytest

chess = pytest.importorskip("chess")

from rl_lab.chess_rl.env import ChessSelfPlayEnv


def test_chess_env_reset_starts_from_initial_board():
    env = ChessSelfPlayEnv()

    board = env.reset()

    assert board.fen() == chess.STARTING_FEN


def test_chess_env_legal_actions_returns_moves():
    env = ChessSelfPlayEnv()
    env.reset()

    actions = env.legal_actions()

    assert "e2e4" in actions
    assert len(actions) == 20
