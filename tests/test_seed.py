import random

import torch

from rl_lab.common.seed import seed_everything


def test_seed_everything_makes_random_repeatable():
    seed_everything(7)
    first_random = random.random()
    first_torch = torch.rand(1).item()

    seed_everything(7)

    assert random.random() == first_random
    assert torch.rand(1).item() == first_torch
