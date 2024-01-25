@pytest.mark.parametrize(
    "path,headers,expected_status,expected_response",
    [
        ("/items", None, 200, {"X-Token values": None}),
        ("/items", {"x-token": "foo"}, 200, {"X-Token values": ["foo"]}),
        # TODO: fix this, is it a bug?
        # ("/items", [("x-token", "foo"), ("x-token", "bar")], 200, {"X-Token values": ["foo", "bar"]}),
    ],
)
def test(path, headers, expected_status, expected_response):
    response = client.get(path, headers=headers)
    assert response.status_code == expected_status
    assert response.json() == expected_response