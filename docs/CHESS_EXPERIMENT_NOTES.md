# Chess Experiment Notes

Chess is included because it shows how quickly reinforcement learning becomes harder when the environment has long-term planning.

## Why Chess Is Harder Than Snake

- The number of legal moves changes every turn.
- Rewards are delayed because the final result may happen many moves later.
- A move can look bad at first but become good later.
- Strong chess play usually needs search, not only a neural network.

## Current Reward Signal

The current experiment uses material changes and game outcomes as a small learning signal. Capturing material gives a short-term signal, while checkmate gives a final signal.

This is intentionally simple. It makes the code readable and gives a clear starting point for future experiments.
