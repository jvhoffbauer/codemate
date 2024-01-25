def test_TilerFactory_WithGdalEnv():
    """test environment_dependency option."""

    router = TilerFactory(
        environment_dependency=lambda: {"GDAL_DISABLE_READDIR_ON_OPEN": "EMPTY_DIR"}
    ).router
    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)

    response = client.get(f"/info?url={DATA_DIR}/non_cog.tif")
    assert not response.json()["overviews"]

    router = TilerFactory(
        environment_dependency=lambda: {"GDAL_DISABLE_READDIR_ON_OPEN": "FALSE"}
    ).router
    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)

    response = client.get(f"/info?url={DATA_DIR}/non_cog.tif")
    assert response.json()["overviews"]

    class ReaddirType(str, Enum):
        false = "false"
        true = "true"
        empty_dir = "empty_dir"

    def gdal_env(disable_read: ReaddirType = Query(ReaddirType.false)):
        return {"GDAL_DISABLE_READDIR_ON_OPEN": disable_read.value.upper()}

    router = TilerFactory(environment_dependency=gdal_env).router
    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)

    response = client.get(f"/info?url={DATA_DIR}/non_cog.tif")
    assert response.json()["overviews"]

    response = client.get(f"/info?url={DATA_DIR}/non_cog.tif&disable_read=false")
    assert response.json()["overviews"]

    response = client.get(f"/info?url={DATA_DIR}/non_cog.tif&disable_read=empty_dir")
    assert not response.json()["overviews"]