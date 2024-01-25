def test_startup():
    app_mod.engine = create_engine("sqlite://")
    app_mod.on_startup()
    insp: Inspector = inspect(app_mod.engine)
    assert insp.has_table(str(app_mod.Hero.__tablename__))