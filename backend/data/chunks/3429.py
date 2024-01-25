@pytest.mark.parametrize(
    "path,expected_status,expected_response",
    [
        ("/default", 200, {"foo": "foo"}),
        ("/default?foo=bar", 200, {"foo": "bar"}),
        ("/required?foo=bar", 200, {"foo": "bar"}),
        ("/required", 422, foo_is_missing),
        ("/required?foo=", 422, foo_is_short),
        ("/multiple?foo=bar", 200, {"foo": "bar"}),
        ("/multiple", 422, foo_is_missing),
        ("/multiple?foo=", 422, foo_is_short),
        ("/unrelated?foo=bar", 200, {"foo": "bar"}),
        ("/unrelated", 422, foo_is_missing),
    ],
)
def test_get(path, expected_status, expected_response):
    response = client.get(path)
    assert response.status_code == expected_status
    assert response.json() == expected_response