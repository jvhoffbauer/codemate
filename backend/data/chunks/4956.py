def test_post_files(tmp_path, app: FastAPI):
    path = tmp_path / "test.txt"
    path.write_bytes(b"<file content>")
    path2 = tmp_path / "test2.txt"
    path2.write_bytes(b"<file content2>")

    client = TestClient(app)
    with path.open("rb") as file, path2.open("rb") as file2:
        response = client.post(
            "/files/",
            files=(
                ("files", ("test.txt", file)),
                ("files", ("test2.txt", file2)),
            ),
        )
    assert response.status_code == 200, response.text
    assert response.json() == {"file_sizes": [14, 15]}