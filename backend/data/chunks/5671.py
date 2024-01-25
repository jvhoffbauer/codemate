def test_MultiBandTilerFactory():
    """test MultiBandTilerFactory."""

    bands = MultiBandTilerFactory(
        reader=BandFileReader, path_dependency=CustomPathParams
    )
    assert len(bands.router.routes) == 28

    app = FastAPI()
    app.include_router(bands.router)

    add_exception_handlers(app, DEFAULT_STATUS_CODES)

    client = TestClient(app)

    response = client.get(f"/bands?directory={DATA_DIR}")
    assert response.status_code == 200
    assert response.json() == ["B01", "B09"]

    # default bands
    response = client.get(f"/info?directory={DATA_DIR}")
    assert response.json()["band_metadata"] == [["B01", {}], ["B09", {}]]

    response = client.get(f"/info?directory={DATA_DIR}&bands=B01")
    assert response.status_code == 200
    assert response.json()["band_metadata"] == [["B01", {}]]

    response = client.get(f"/info.geojson?directory={DATA_DIR}&bands=B01")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    assert response.json()["properties"]["band_metadata"] == [["B01", {}]]

    # need bands or expression
    response = client.get(f"/preview.tif?directory={DATA_DIR}&return_mask=false")
    assert response.status_code == 400

    response = client.get(
        f"/preview.tif?directory={DATA_DIR}&bands=B01&bands=B09&bands=B01&return_mask=false"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["dtype"] == "uint16"
    assert meta["count"] == 3

    response = client.get(
        "/preview.tif",
        params={
            "directory": DATA_DIR,
            "expression": "B01;B09;B01",
            "return_mask": False,
        },
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert (
        meta["dtype"] == "int32"
    )  # when using expression, numexpr will change the datatype
    assert meta["count"] == 3

    # GET - statistics
    response = client.get(f"/statistics?directory={DATA_DIR}")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    resp = response.json()
    assert len(resp) == 2
    assert resp["B01"]
    assert resp["B09"]

    response = client.get(f"/statistics?directory={DATA_DIR}&bands=B01&bands=B09")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    resp = response.json()
    assert len(resp) == 2
    assert set(resp["B01"].keys()) == {
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
    assert resp["B09"]

    response = client.get(f"/statistics?directory={DATA_DIR}&expression=B01/B09")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    resp = response.json()
    assert len(resp) == 1
    assert set(resp["B01/B09"].keys()) == {
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

    # POST - statistics
    band_feature = {
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

    response = client.post(
        f"/statistics?directory={DATA_DIR}&bands=B01&bands=B09",
        json=band_feature["features"][0],
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    resp = response.json()
    props = resp["properties"]["statistics"]
    assert len(props) == 2
    assert set(props["B01"].keys()) == {
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
    assert props["B09"]

    response = client.post(
        f"/statistics?directory={DATA_DIR}&expression=B01/B09",
        json=band_feature["features"][0],
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    resp = response.json()
    props = resp["properties"]["statistics"]
    assert len(props) == 1
    assert set(props["B01/B09"].keys()) == {
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

    response = client.post(
        f"/statistics?directory={DATA_DIR}&bands=B01&bands=B09", json=band_feature
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    resp = response.json()
    props = resp["features"][0]["properties"]["statistics"]
    assert len(props) == 2
    assert set(props["B01"].keys()) == {
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
    assert props["B09"]

    response = client.post(
        f"/statistics?directory={DATA_DIR}&expression=B01/B09", json=band_feature
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    resp = response.json()
    props = resp["features"][0]["properties"]["statistics"]
    assert len(props) == 1
    assert set(props["B01/B09"].keys()) == {
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

    # default bands
    response = client.post(f"/statistics?directory={DATA_DIR}", json=band_feature)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    resp = response.json()
    props = resp["features"][0]["properties"]["statistics"]
    assert props["B01"]
    assert props["B09"]

    response = client.post(
        f"/statistics?directory={DATA_DIR}",
        json=band_feature["features"][0],
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    resp = response.json()
    props = resp["properties"]["statistics"]
    assert props["B01"]
    assert props["B09"]