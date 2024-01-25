@pytest.mark.parametrize(
    "path,expected_status,expected_response",
    [
        ("/items/", 200, [{"name": "Foo", "price": 42}]),
        ("/users/", 200, [{"username": "johndoe"}]),
        ("/elements/", 200, [{"item_id": "Foo"}]),
    ],
)
def test_query_params_str_validations(path, expected_status, expected_response):
    response = client.get(path)
    assert response.status_code == expected_status
    assert response.json() == expected_response