@needs_py39
def test_override_in_users():
    from docs_src.dependency_testing.tutorial001_an_py39 import client

    response = client.get("/users/")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "message": "Hello Users!",
        "params": {"q": None, "skip": 5, "limit": 10},
    }