def test_post_large_file(tmp_path, client: TestClient):
    default_pydantic_max_size = 2**16
    path = tmp_path / "test.txt"
    path.write_bytes(b"x" * (default_pydantic_max_size + 1))

    with path.open("rb") as file:
        response = client.post("/files/", files={"file": file})
    assert response.status_code == 200, response.text
    assert response.json() == {"file_size": default_pydantic_max_size + 1}