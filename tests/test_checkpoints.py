from rl_lab.common.checkpoints import checkpoint_path


def test_checkpoint_path_adds_pt_suffix_and_directory():
    path = checkpoint_path("snake", "demo")

    assert str(path).replace("\\", "/") == "checkpoints/snake_demo.pt"
