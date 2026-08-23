from rl_lab.common.replay import ReplayMemory


def test_replay_memory_keeps_recent_experiences():
    memory = ReplayMemory(capacity=2, seed=1)

    memory.push("first")
    memory.push("second")
    memory.push("third")

    assert len(memory) == 2
    assert list(memory.buffer) == ["second", "third"]


def test_replay_memory_samples_requested_batch_size():
    memory = ReplayMemory(capacity=5, seed=1)
    for number in range(5):
        memory.push(number)

    sample = memory.sample(3)

    assert len(sample) == 3
    assert set(sample).issubset(set(range(5)))
