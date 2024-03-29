@pytest.mark.xfail
def test_withoutCustomRoute(monkeypatch):
    """Create App."""
    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "something")

    app = FastAPI()
    router = APIRouter()

    def f(r):
        return get_gdal_config("GDAL_DISABLE_READDIR_ON_OPEN")

    @router.get("/simple")
    def home():
        """Works and should return FALSE."""
        with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="FALSE"):
            res = get_gdal_config("GDAL_DISABLE_READDIR_ON_OPEN")
        return {"env": res}

    @router.get("/asimple")
    async def home1():
        """Works and should return FALSE."""
        with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="FALSE"):
            res = get_gdal_config("GDAL_DISABLE_READDIR_ON_OPEN")
        return {"env": res}

    @router.get("/future")
    def home2():
        """Doesn't work and should return the value from env."""
        with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="FALSE"):
            with futures.ThreadPoolExecutor() as executor:
                res = list(executor.map(f, range(1)))[0]
        return {"env": res}

    @router.get("/afuture")
    async def home3():
        """Works and should return FALSE."""
        with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="FALSE"):
            with futures.ThreadPoolExecutor() as executor:
                res = list(executor.map(f, range(1)))[0]
        return {"env": res}

    app.include_router(router)
    client = TestClient(app)

    response = client.get("/simple")
    assert response.json()["env"] == "FALSE"

    response = client.get("/asimple")
    assert response.json()["env"] == "FALSE"

    # confirm the multi threads case doesn't work
    response = client.get("/future")
    assert not response.json()["env"] == "FALSE"

    response = client.get("/afuture")
    assert response.json()["env"] == "FALSE"