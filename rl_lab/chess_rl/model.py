import torch
from torch import nn


class ChessPolicyNet(nn.Module):
    def __init__(self, hidden_size: int = 128):
        super().__init__()
        self.net = nn.Sequential(
            nn.Flatten(),
            nn.Linear(12 * 8 * 8, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, 1),
        )

    def forward(self, board_tensor: torch.Tensor) -> torch.Tensor:
        return self.net(board_tensor.float())
