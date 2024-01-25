def prepare_fixture(clear_sqlmodel):
    # Trigger side effects of registering table models in SQLModel
    # This has to be called after clear_sqlmodel, but before the session_fixture
    # That's why the extra custom fixture here
    importlib.reload(app_mod)