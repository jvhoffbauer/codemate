def test_custom_middleware_exception(tmp_path: Path):
    default_pydantic_max_size = 2**16
    path = tmp_path / "test.txt"
    path.write_bytes(b"x" * (default_pydantic_max_size + 1))

    with client:
        with open(path, "rb") as file:
            response = client.post("/middleware", files={"file": file})
        assert response.status_code == 422, response.text
        assert response.json() == {
            "detail": {
                "name": "ContentSizeLimitExceeded",
                "code": 999,
                "message": "File limit exceeded",
            }
        }