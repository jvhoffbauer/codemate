def test_settings_valid_url():
    settings = Settings(site_url="/")
    assert settings.site_url == ""
    settings = Settings(amis_cdn="https://unpkg.com/")
    assert settings.amis_cdn == "https://unpkg.com"
    settings = Settings(site_path="/admin/")
    assert settings.site_path == "/admin"
    settings = Settings(site_path="/admin")
    assert settings.site_path == "/admin"