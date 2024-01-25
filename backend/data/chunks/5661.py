@patch("rio_tiler.io.rasterio.rasterio")
def test_MultiBaseTilerFactory(rio):
    """test MultiBaseTilerFactory."""
    rio.open = mock_rasterio_open

    stac = MultiBaseTilerFactory(reader=STACReader)
    assert len(stac.router.routes) == 29

    app = FastAPI()
    app.include_router(stac.router)

    add_exception_handlers(app, DEFAULT_STATUS_CODES)

    client = TestClient(app)

    response = client.get(f"/assets?url={DATA_DIR}/item.json")
    assert response.status_code == 200
    assert len(response.json()) == 2

    response = client.get(f"/bounds?url={DATA_DIR}/item.json")
    assert response.status_code == 200
    assert len(response.json()["bounds"]) == 4

    response = client.get(f"/info?url={DATA_DIR}/item.json")
    assert response.status_code == 200
    assert len(response.json()) == 2

    response = client.get(f"/info?url={DATA_DIR}/item.json&assets=B01&assets=B09")
    assert response.status_code == 200
    assert response.json()["B01"]
    assert response.json()["B09"]

    response = client.get(f"/info.geojson?url={DATA_DIR}/item.json&assets=B01")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    assert response.json()["type"] == "Feature"

    response = client.get(f"/preview.tif?url={DATA_DIR}/item.json")
    assert response.status_code == 400

    response = client.get(
        f"/preview.tif?url={DATA_DIR}/item.json&assets=B01&assets=B09&return_mask=false"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["dtype"] == "uint16"
    assert meta["count"] == 2

    response = client.get(
        "/preview.tif",
        params={
            "url": f"{DATA_DIR}/item.json",
            "expression": "B01_b1;B01_b1;B01_b1",
            "return_mask": False,
        },
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["dtype"] == "int32"
    assert meta["count"] == 3

    response = client.get(
        f"/preview.tif?url={DATA_DIR}/item.json&assets=B01&asset_bidx=B01|1,1,1&return_mask=false"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["dtype"] == "uint16"
    assert meta["count"] == 3

    response = client.get(
        "/preview.tif",
        params={
            "url": f"{DATA_DIR}/item.json",
            "expression": "B01_b1;B01_b1;B01_b1",
            "return_mask": False,
        },
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["dtype"] == "int32"
    assert meta["count"] == 3

    # Use asset_as_band option
    response = client.get(
        "/preview.tif",
        params={
            "url": f"{DATA_DIR}/item.json",
            "expression": "B01;B01;B01",
            "asset_as_band": True,
            "return_mask": False,
        },
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["dtype"] == "int32"
    assert meta["count"] == 3

    # GET - statistics
    response = client.get(
        f"/asset_statistics?url={DATA_DIR}/item.json&assets=B01&assets=B09"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    resp = response.json()
    assert len(resp) == 2
    assert set(resp["B01"]["b1"].keys()) == {
        "min",
        "max",
        "mean",
        "count",
        "sum",
        "std",
        "median",
        "majority",
        "minority",
        "unique",
        "histogram",
        "valid_percent",
        "masked_pixels",
        "valid_pixels",
        "percentile_2",
        "percentile_98",
    }
    response = client.get(
        f"/asset_statistics?url={DATA_DIR}/item.json&assets=B01&assets=B09&asset_bidx=B01|1&asset_bidx=B09|1"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    resp = response.json()
    assert len(resp) == 2
    assert resp["B01"]["b1"]
    assert resp["B09"]["b1"]

    response = client.get(f"/statistics?url={DATA_DIR}/item.json&assets=B01&assets=B09")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    resp = response.json()
    assert list(resp) == ["B01_b1", "B09_b1"]
    assert set(resp["B01_b1"].keys()) == {
        "min",
        "max",
        "mean",
        "count",
        "sum",
        "std",
        "median",
        "majority",
        "minority",
        "unique",
        "histogram",
        "valid_percent",
        "masked_pixels",
        "valid_pixels",
        "percentile_2",
        "percentile_98",
    }

    response = client.get(
        f"/statistics?url={DATA_DIR}/item.json&assets=B01&assets=B09&asset_bidx=B01|1&asset_bidx=B09|1"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    resp = response.json()
    assert len(resp) == 2
    assert resp["B01_b1"]
    assert resp["B09_b1"]

    stac_feature = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [23.62060546875, 31.834399275715842],
                            [23.838958740234375, 31.834399275715842],
                            [23.838958740234375, 32.072101858328686],
                            [23.62060546875, 32.072101858328686],
                            [23.62060546875, 31.834399275715842],
                        ]
                    ],
                },
            }
        ],
    }

    # POST - statistics
    response = client.post(
        f"/statistics?url={DATA_DIR}/item.json&assets=B01&assets=B09",
        json=stac_feature["features"][0],
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    resp = response.json()
    props = resp["properties"]["statistics"]
    assert len(props) == 2
    assert set(props["B01_b1"].keys()) == {
        "min",
        "max",
        "mean",
        "count",
        "sum",
        "std",
        "median",
        "majority",
        "minority",
        "unique",
        "histogram",
        "valid_percent",
        "masked_pixels",
        "valid_pixels",
        "percentile_2",
        "percentile_98",
    }
    assert props["B09_b1"]

    response = client.post(
        f"/statistics?url={DATA_DIR}/item.json&assets=B01&assets=B09", json=stac_feature
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    resp = response.json()
    props = resp["features"][0]["properties"]["statistics"]
    assert len(props) == 2
    assert set(props["B01_b1"].keys()) == {
        "min",
        "max",
        "mean",
        "count",
        "sum",
        "std",
        "median",
        "majority",
        "minority",
        "unique",
        "histogram",
        "valid_percent",
        "masked_pixels",
        "valid_pixels",
        "percentile_2",
        "percentile_98",
    }
    assert props["B09_b1"]

    response = client.post(
        f"/statistics?url={DATA_DIR}/item.json&assets=B01&assets=B09&asset_bidx=B01|1&asset_bidx=B09|1",
        json=stac_feature["features"][0],
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    resp = response.json()
    props = resp["properties"]["statistics"]
    assert len(props) == 2
    assert set(props["B01_b1"].keys()) == {
        "min",
        "max",
        "mean",
        "count",
        "sum",
        "std",
        "median",
        "majority",
        "minority",
        "unique",
        "histogram",
        "valid_percent",
        "masked_pixels",
        "valid_pixels",
        "percentile_2",
        "percentile_98",
    }
    assert props["B09_b1"]