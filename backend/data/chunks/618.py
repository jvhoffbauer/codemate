def prepare_fixture(clear_sqlmodel):
    # Trigger side effects of registering table models in SQLModel
    # This has to be called after clear_sqlmodel
    importlib.reload(app_mod)
    importlib.reload(test_mod)