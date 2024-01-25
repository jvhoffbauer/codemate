@pytest.mark.parametrize("compress", [True, False])
def test_gzip_request(compress):
    n = 1000
    headers = {}
    body = [1] * n
    data = json.dumps(body).encode()
    if compress:
        data = gzip.compress(data)
        headers["Content-Encoding"] = "gzip"
    headers["Content-Type"] = "application/json"
    response = client.post("/sum", content=data, headers=headers)
    assert response.json() == {"sum": n}