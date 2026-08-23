from rl_lab.common.config import load_json_config


def test_load_json_config_reads_file(tmp_path):
    config_file = tmp_path / "config.json"
    config_file.write_text('{"episodes": 5}', encoding="utf-8")

    assert load_json_config(config_file) == {"episodes": 5}
