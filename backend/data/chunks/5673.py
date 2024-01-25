def test_TilerFactory_WithDependencies():
    """Test TilerFactory class."""

    http_basic = security.HTTPBasic()

    def must_be_bob(credentials: security.HTTPBasicCredentials = Depends(http_basic)):
        if credentials.username == "bob":
            return True
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You're not Bob",
            headers={"WWW-Authenticate": "Basic"},
        )

    cog = TilerFactory(
        route_dependencies=[
            (
                [
                    {"path": "/bounds", "method": "GET"},
                    {"path": "/tiles/{z}/{x}/{y}", "method": "GET"},
                ],
                [Depends(must_be_bob)],
            ),
        ],
        router_prefix="something",
    )
    assert len(cog.router.routes) == 27

    app = FastAPI()
    app.include_router(cog.router, prefix="/something")
    client = TestClient(app)

    auth_bob = httpx.BasicAuth(username="bob", password="ILoveSponge")
    auth_notbob = httpx.BasicAuth(username="notbob", password="IHateSponge")

    response = client.get(f"/something/tilejson.json?url={DATA_DIR}/cog.tif")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json()["tilejson"]

    response = client.get(
        f"/something/bounds?url={DATA_DIR}/cog.tif&rescale=0,1000", auth=auth_bob
    )
    assert response.status_code == 200

    response = client.get(
        f"/something/bounds?url={DATA_DIR}/cog.tif&rescale=0,1000", auth=auth_notbob
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "You're not Bob"

    response = client.get(
        f"/something/tiles/8/87/48?url={DATA_DIR}/cog.tif&rescale=0,1000", auth=auth_bob
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"

    response = client.get(
        f"/something/tiles/8/87/48?url={DATA_DIR}/cog.tif&rescale=0,1000",
        auth=auth_notbob,
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "You're not Bob"

    response = client.get(
        f"/something/tiles/8/87/48.jpeg?url={DATA_DIR}/cog.tif&rescale=0,1000"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"

    cog = TilerFactory(router_prefix="something")
    cog.add_route_dependencies(
        scopes=[{"path": "/bounds", "method": "GET"}],
        dependencies=[Depends(must_be_bob)],
    )

    app = FastAPI()
    app.include_router(cog.router, prefix="/something")
    client = TestClient(app)

    response = client.get(f"/something/tilejson.json?url={DATA_DIR}/cog.tif")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json()["tilejson"]

    response = client.get(
        f"/something/bounds?url={DATA_DIR}/cog.tif&rescale=0,1000", auth=auth_bob
    )
    assert response.status_code == 200

    response = client.get(
        f"/something/bounds?url={DATA_DIR}/cog.tif&rescale=0,1000", auth=auth_notbob
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "You're not Bob"