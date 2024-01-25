@needs_py39
def test_post_file(tmp_path, client: TestClient):
    path = tmp_path / "test.txt"
    path.write_bytes(b"<file content>")

    with path.open("rb") as file:
        response = client.post("/files/", files={"file": file})
    assert response.status_code == 200, response.text
    assert response.json() == {"file_size": 14}