from pathlib import Path


def checkpoint_path(agent_name: str, run_name: str, root: str = "checkpoints") -> Path:
    return Path(root) / f"{agent_name}_{run_name}.pt"
