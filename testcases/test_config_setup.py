import importlib

import utilities.read_properties as read_properties


def test_config_loader_uses_project_root(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    importlib.reload(read_properties)

    assert read_properties.ReadConfig.get_url().startswith("https://")
    assert read_properties.ReadConfig.get_product() == "Laptop"
