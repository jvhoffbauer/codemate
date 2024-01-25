@needs_py39
def test_post_files_and_token(tmp_path, app: FastAPI):
    patha = tmp_path / "test.txt"
    pathb = tmp_path / "testb.txt"
    patha.write_text("<file content>")
    pathb.write_text("<file b content>")

    client = TestClient(app)
    with patha.open("rb") as filea, pathb.open("rb") as fileb:
        response = client.post(
            "/files/",
            data={"token": "foo"},
            files={"file": filea, "fileb": ("testb.txt", fileb, "text/plain")},
        )
    assert response.status_code == 200, response.text
    assert response.json() == {
        "file_size": 14,
        "token": "foo",
        "fileb_content_type": "text/plain",
    }