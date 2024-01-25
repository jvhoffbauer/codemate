def test_file_path():
    response = client.get("/files/home/johndoe/myfile.txt")
    print(response.content)
    assert response.status_code == 200, response.text
    assert response.json() == {"file_path": "home/johndoe/myfile.txt"}