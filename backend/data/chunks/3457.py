@pytest.mark.parametrize(
    "path,expected_status,expected_response",
    [
        (
            "/hidden_query",
            200,
            {"hidden_query": None},
        ),
        (
            "/hidden_query?hidden_query=somevalue",
            200,
            {"hidden_query": "somevalue"},
        ),
    ],
)
def test_hidden_query(path, expected_status, expected_response):
    client = TestClient(app)
    response = client.get(path)
    assert response.status_code == expected_status
    assert response.json() == expected_response