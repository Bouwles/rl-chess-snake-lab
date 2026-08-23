# Reinforcement Learning Concepts

Reinforcement learning is about learning through actions and rewards.

## Agent

The agent is the learner. In this repo, the Snake agent chooses turns and the Chess agent chooses legal moves.

## Environment

The environment is the world the agent acts inside. It gives the agent a state, accepts an action, and returns a reward.

## State

The state is what the agent can see. Snake uses 11 numbers for dangers, direction, and food location. Chess uses board feature planes.

## Action

An action is a choice. Snake has three actions: turn left, go straight, or turn right. Chess actions are legal UCI moves like `e2e4`.

## Reward

The reward tells the agent whether an action was useful. Eating food is good, dying is bad, and chess material changes are used as a simple learning signal.

## Exploration

Exploration means trying actions that may not look best yet. The Snake DQN uses epsilon-greedy exploration so it does not repeat the same early mistakes forever.
