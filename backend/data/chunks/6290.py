def test_settings_valid_database_url():
    settings = Settings()
    assert settings.database_url_async
    settings = Settings(
        database_url_async="sqlite+aiosqlite:///amisadmin.db?check_same_thread=False"
    )
    assert settings.database_url == ""
    assert settings.database_url_async
    settings = Settings(database_url="sqlite:///amisadmin.db?check_same_thread=False")
    assert settings.database_url
    assert settings.database_url_async == ""