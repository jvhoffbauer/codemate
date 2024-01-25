@pytest.mark.xfail
def test_withCustomRoute(monkeypatch):
    """Create App."""
    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "something")

    app = FastAPI()

    env = {"GDAL_DISABLE_READDIR_ON_OPEN": "FALSE"}
    with pytest.warns(DeprecationWarning):
        route_class = apiroute_factory(env)
    router = APIRouter(route_class=route_class)

    def f(r):
        return get_gdal_config("GDAL_DISABLE_READDIR_ON_OPEN")

    @router.get("/simple")
    def home():
        """Works and should return FALSE."""
        res = get_gdal_config("GDAL_DISABLE_READDIR_ON_OPEN")
        return {"env": res}

    @router.get("/asimple")
    async def home1():
        """Works and should return FALSE."""
        res = get_gdal_config("GDAL_DISABLE_READDIR_ON_OPEN")
        return {"env": res}

    @router.get("/future")
    def home2():
        """Doesn't work and should return the value from env."""
        with futures.ThreadPoolExecutor() as executor:
            res = list(executor.map(f, range(1)))[0]
        return {"env": res}

    @router.get("/afuture")
    async def home3():
        """Works and should return FALSE."""
        with futures.ThreadPoolExecutor() as executor:
            res = list(executor.map(f, range(1)))[0]
        return {"env": res}

    app.include_router(router)
    client = TestClient(app)

    response = client.get("/simple")
    assert response.json()["env"] == "FALSE"

    response = client.get("/asimple")
    assert response.json()["env"] == "FALSE"

    # confirm the Custom APIRoute class fix
    response = client.get("/future")
    assert response.json()["env"] == "FALSE"

    response = client.get("/afuture")
    assert response.json()["env"] == "FALSE"