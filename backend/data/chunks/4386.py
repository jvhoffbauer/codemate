def test_get():
    response = client.get("/typer", follow_redirects=False)
    assert response.status_code == 307, response.text
    assert response.headers["location"] == "https://typer.tiangolo.com"