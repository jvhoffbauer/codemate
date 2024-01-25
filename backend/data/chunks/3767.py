@needs_pydanticv2
def test_override_settings():
    from docs_src.settings.app02 import test_main

    test_main.test_app()