def test_TMSFactory():
    """test TMSFactory."""

    tms_endpoints = TMSFactory(router_prefix="tms")
    assert len(tms_endpoints.router.routes) == 2

    app = FastAPI()
    app.include_router(tms_endpoints.router, prefix="/tms")

    client = TestClient(app)

    response = client.get("/tms/tileMatrixSets")
    assert response.status_code == 200
    body = response.json()
    assert len(body["tileMatrixSets"]) == NB_DEFAULT_TMS
    tms = list(filter(lambda m: m["id"] == "WebMercatorQuad", body["tileMatrixSets"]))[
        0
    ]
    assert (
        tms["links"][0]["href"]
        == "http://testserver/tms/tileMatrixSets/WebMercatorQuad"
    )

    response = client.get("/tms/tileMatrixSets/WebMercatorQuad")
    assert response.status_code == 200
    body = response.json()
    assert body["type"] == "TileMatrixSetType"
    assert body["identifier"] == "WebMercatorQuad"

    response = client.get("/tms/tileMatrixSets/WebMercatorQua")
    assert response.status_code == 422

    app = FastAPI()
    tms_endpoints = TMSFactory(supported_tms=WEB_TMS)
    app.include_router(
        tms_endpoints.router,
    )

    client = TestClient(app)

    response = client.get("/tileMatrixSets")
    assert response.status_code == 200
    body = response.json()
    assert len(body["tileMatrixSets"]) == 1

    response = client.get("/tileMatrixSets/WebMercatorQuad")
    assert response.status_code == 200

    response = client.get("/tileMatrixSets/LINZAntarticaMapTilegrid")
    assert response.status_code == 422