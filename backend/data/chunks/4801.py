@needs_py39
def test_get_password_hash():
    from docs_src.security.tutorial005_py39 import get_password_hash

    assert get_password_hash("secretalice")