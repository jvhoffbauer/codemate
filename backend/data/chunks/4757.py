@needs_py310
def test_get_password_hash():
    from docs_src.security.tutorial005_an_py310 import get_password_hash

    assert get_password_hash("secretalice")