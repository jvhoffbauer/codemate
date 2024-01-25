def test_custom_middleware_exception_not_raised(tmp_path: Path):
    path = tmp_path / "test.txt"
    path.write_bytes(b"<file content>")

    with client:
        with open(path, "rb") as file:
            response = client.post("/middleware", files={"file": file})
        assert response.status_code == 200, response.text
        assert response.json() == {"message": "OK"}