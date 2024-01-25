def test_CustomPath():
    """Test Custom Render Params dependency."""
    app = FastAPI()

    cog = TilerFactory(path_dependency=CustomPathParams)
    app.include_router(cog.router)
    client = TestClient(app)

    response = client.get("/preview.png?file=cog.tif&rescale=0,10000")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"

    response = client.get("/preview.png?file=somethingelse.jpeg")
    assert "valid File" in response.text
    assert response.status_code == 400

    response = client.get("/preview.png?file=somethingelse.tif&rescale=0,10000")
    assert "exists" in response.text
    assert response.status_code == 404