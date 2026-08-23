# Snake Reward Design

The Snake environment uses simple rewards so the learning loop stays easy to understand.

## Rewards

- `+10.0` when the snake eats food
- `-10.0` when the snake dies
- `-0.01` for a normal move

The small negative reward for normal movement encourages the agent to find food instead of wandering forever.

## State Inputs

The agent receives 11 values:

- danger on the left
- danger straight ahead
- danger on the right
- current direction as four values
- food location compared with the snake head

This state is small, but it is enough to learn basic survival and food-seeking behavior.
