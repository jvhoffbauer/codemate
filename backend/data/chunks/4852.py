@needs_py39
def test_create_access_token():
    from docs_src.security.tutorial005_an_py39 import create_access_token

    access_token = create_access_token(data={"data": "foo"})
    assert access_token