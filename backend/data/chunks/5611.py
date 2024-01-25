def test_dataset():
    """test dataset deps."""

    app = FastAPI()

    @app.get("/", response_class=JSONResponse)
    def _endpoint(params=Depends(dependencies.DatasetParams)):
        """return params."""
        return params

    @app.get("/nan", response_class=JSONResponse)
    def is_nan(params=Depends(dependencies.DatasetParams)):
        """return params."""
        return str(params.nodata)

    client = TestClient(app)
    response = client.get("/")
    assert not response.json()["nodata"]
    assert not response.json()["unscale"]
    assert response.json()["resampling_method"] == "nearest"

    response = client.get("/?resampling=cubic")
    assert not response.json()["nodata"]
    assert not response.json()["unscale"]
    assert response.json()["resampling_method"] == "cubic"

    response = client.get("/?nodata=10")
    assert response.json()["nodata"] == 10.0

    response = client.get("/nan?nodata=nan")
    assert response.json() == "nan"