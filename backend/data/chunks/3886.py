def test_path_operation_img():
    shutil.copy("./docs/en/docs/img/favicon.png", "./image.png")
    response = client.get("/items/foo?img=1")
    assert response.status_code == 200, response.text
    assert response.headers["Content-Type"] == "image/png"
    assert len(response.content)
    os.remove("./image.png")