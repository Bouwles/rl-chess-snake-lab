# Project Summary

This project explores reinforcement learning through two game environments with different levels of difficulty.

The Snake section focuses on a compact DQN setup. It includes a custom environment, a Gymnasium wrapper, replay memory, epsilon-greedy exploration, baseline policies, and evaluation helpers.

The Chess section explores self-play with legal move generation, board feature encoding, a small PyTorch value network, and a simple reward signal based on material changes and game outcomes.

The main goal is not to build unbeatable game agents. The goal is to show the full learning loop: state, action, reward, memory, model update, evaluation, and limitations.
