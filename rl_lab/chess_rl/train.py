import random

import chess
import torch
from torch import optim

from rl_lab.chess_rl.env import ChessSelfPlayEnv
from rl_lab.chess_rl.features import board_to_tensor
from rl_lab.chess_rl.model import ChessPolicyNet


def pick_material_move(board: chess.Board, exploration: float = 0.25) -> str:
    legal_moves = list(board.legal_moves)
    if random.random() < exploration:
        return random.choice(legal_moves).uci()

    scored_moves = []
    for move in legal_moves:
        test_board = board.copy()
        test_board.push(move)
        capture_score = 1 if board.is_capture(move) else 0
        check_score = 0.25 if test_board.is_check() else 0
        scored_moves.append((capture_score + check_score, move.uci()))

    return max(scored_moves)[1]


def train_chess_self_play(episodes: int = 10) -> ChessPolicyNet:
    env = ChessSelfPlayEnv()
    model = ChessPolicyNet()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for _ in range(episodes):
        board = env.reset()
        done = False
        while not done:
            action = pick_material_move(board)
            tensor = torch.tensor(board_to_tensor(board)).unsqueeze(0)
            value = model(tensor).squeeze()
            board, reward, done, _ = env.step(action)
            loss = (value - reward) ** 2
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    return model


if __name__ == "__main__":
    torch.save(train_chess_self_play().state_dict(), "chess_policy.pt")
