def test_settings(monkeypatch: MonkeyPatch):
    from docs_src.settings.app02 import main

    monkeypatch.setenv("ADMIN_EMAIL", "admin@example.com")
    settings = main.get_settings()
    assert settings.app_name == "Awesome API"
    assert settings.items_per_user == 50