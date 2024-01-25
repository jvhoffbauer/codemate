def test_cookie_is_set_once():
    direct_response = client.get("/directCookie")
    indirect_response = client.get("/indirectCookie")
    assert (
        direct_response.headers["set-cookie"] == indirect_response.headers["set-cookie"]
    )