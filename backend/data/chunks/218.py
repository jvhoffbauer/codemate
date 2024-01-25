def test_get_session():
    app_mod.engine = create_engine("sqlite://")
    for session in app_mod.get_session():
        assert isinstance(session, Session)
        assert session.bind == app_mod.engine