def test_override_server_error_exception_raises():
    with pytest.raises(RuntimeError):
        client.get("/server-error")