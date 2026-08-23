import chess

from .features import material_score


class ChessSelfPlayEnv:
    """Gym-style chess environment powered by python-chess legal moves."""

    def __init__(self, max_moves: int = 160):
        self.max_moves = max_moves
        self.board = chess.Board()
        self.ply_count = 0

    def reset(self) -> chess.Board:
        self.board = chess.Board()
        self.ply_count = 0
        return self.board.copy()

    def legal_actions(self) -> list[str]:
        return [move.uci() for move in self.board.legal_moves]

    def step(self, action: str) -> tuple[chess.Board, float, bool, dict[str, str]]:
        move = chess.Move.from_uci(action)
        if move not in self.board.legal_moves:
            raise ValueError(f"Illegal chess move: {action}")

        before = material_score(self.board)
        self.board.push(move)
        after = material_score(self.board)
        self.ply_count += 1

        done = self.board.is_game_over() or self.ply_count >= self.max_moves
        reward = (after - before) / 9.0

        if self.board.is_checkmate():
            reward = 1.0 if self.board.turn == chess.BLACK else -1.0
        elif done:
            reward = 0.0

        return self.board.copy(), reward, done, {"turn": "white" if self.board.turn else "black"}
