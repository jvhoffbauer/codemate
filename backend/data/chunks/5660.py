def test_TilerFactory():
    """Test TilerFactory class."""
    cog = TilerFactory()
    assert len(cog.router.routes) == 27
    assert len(cog.supported_tms.list()) == NB_DEFAULT_TMS

    cog = TilerFactory(router_prefix="something", supported_tms=WEB_TMS)
    assert len(cog.supported_tms.list()) == 1

    app = FastAPI()
    app.include_router(cog.router, prefix="/something")
    client = TestClient(app)

    response = client.get(f"/something/tilejson.json?url={DATA_DIR}/cog.tif")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json()["tilejson"]

    response = client.get(f"/something/NZTM2000/tilejson.json?url={DATA_DIR}/cog.tif")
    assert response.status_code == 422

    cog = TilerFactory(add_preview=False, add_part=False, add_viewer=False)
    assert len(cog.router.routes) == 18

    app = FastAPI()
    cog = TilerFactory()
    app.include_router(cog.router)

    add_exception_handlers(app, DEFAULT_STATUS_CODES)

    client = TestClient(app)

    response = client.get(f"/tiles/8/87/48?url={DATA_DIR}/cog.tif&rescale=0,1000")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    response = client.get(
        f"/tiles/8/87/48?url={DATA_DIR}/cog.tif&rescale=-3.4028235e+38,3.4028235e+38"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"

    response = client.get(
        f"/tiles/8/87/48.tif?url={DATA_DIR}/cog.tif&bidx=1&bidx=1&bidx=1&return_mask=false"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["dtype"] == "uint16"
    assert meta["count"] == 3
    assert meta["width"] == 256
    assert meta["height"] == 256

    response = client.get(
        "/tiles/8/87/48.tif",
        params={
            "url": f"{DATA_DIR}/cog.tif",
            "expression": "b1;b1;b1",
            "return_mask": False,
        },
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["dtype"] == "int32"
    assert meta["count"] == 3
    assert meta["width"] == 256
    assert meta["height"] == 256

    response = client.get(
        f"/tiles/8/84/47?url={DATA_DIR}/cog.tif&bidx=1&rescale=0,1000&colormap_name=viridis"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"

    # Dict
    cmap = urlencode(
        {
            "colormap": json.dumps(
                {
                    "1": [58, 102, 24, 255],
                    "2": [100, 177, 41],
                    "3": "#b1b129",
                    "4": "#ddcb9aFF",
                }
            )
        }
    )
    response = client.get(f"/tiles/8/84/47.png?url={DATA_DIR}/cog.tif&bidx=1&{cmap}")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"

    # Intervals
    cmap = urlencode(
        {
            "colormap": json.dumps(
                [
                    # ([min, max], [r, g, b, a])
                    ([1, 2], [0, 0, 0, 255]),
                    ([2, 3], [255, 255, 255, 255]),
                    ([3, 1000], [255, 0, 0, 255]),
                ]
            )
        }
    )
    response = client.get(f"/tiles/8/84/47.png?url={DATA_DIR}/cog.tif&bidx=1&{cmap}")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"

    # Bad colormap format
    cmap = urlencode({"colormap": json.dumps({"1": [58, 102]})})
    response = client.get(f"/tiles/8/84/47.png?url={DATA_DIR}/cog.tif&bidx=1&{cmap}")
    assert response.status_code == 400

    # no json encoding
    cmap = urlencode({"colormap": {"1": [58, 102]}})
    response = client.get(f"/tiles/8/84/47.png?url={DATA_DIR}/cog.tif&bidx=1&{cmap}")
    assert response.status_code == 400

    # Test NumpyTile
    response = client.get(f"/tiles/8/87/48.npy?url={DATA_DIR}/cog.tif")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/x-binary"
    npy_tile = numpy.load(BytesIO(response.content))
    assert npy_tile.shape == (2, 256, 256)  # mask + data

    # Test Buffer
    response = client.get(f"/tiles/8/87/48.npy?url={DATA_DIR}/cog.tif&buffer=10")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/x-binary"
    npy_tile = numpy.load(BytesIO(response.content))
    assert npy_tile.shape == (2, 276, 276)  # mask + data

    response = client.get(
        f"/preview?url={DATA_DIR}/cog.tif&rescale=0,1000&max_size=256"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"

    response = client.get(
        f"/crop/-56.228,72.715,-54.547,73.188.png?url={DATA_DIR}/cog.tif&rescale=0,1000&max_size=256"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"

    response = client.get(f"/point/-56.228,72.715?url={DATA_DIR}/cog.tif")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert len(response.json()["values"]) == 1
    assert response.json()["band_names"] == ["b1"]

    response = client.get(f"/point/-56.228,72.715?url={DATA_DIR}/cog.tif&bidx=1&bidx=1")
    assert len(response.json()["values"]) == 2
    assert response.json()["band_names"] == ["b1", "b1"]

    response = client.get(
        f"/point/-56.228,72.715?url={DATA_DIR}/cog.tif&expression=b1*2"
    )
    assert len(response.json()["values"]) == 1
    assert response.json()["band_names"] == ["b1*2"]

    response = client.get(f"/tilejson.json?url={DATA_DIR}/cog.tif")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json()["tilejson"]

    response = client.get(f"/WorldCRS84Quad/tilejson.json?url={DATA_DIR}/cog.tif")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json()["tilejson"]

    response_qs = client.get(
        f"/tilejson.json?url={DATA_DIR}/cog.tif&TileMatrixSetId=WorldCRS84Quad"
    )
    assert response.json()["tiles"] == response_qs.json()["tiles"]

    response = client.get(f"/tilejson.json?url={DATA_DIR}/cog.tif&tile_format=png")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json()["tilejson"]
    assert "png" in response.json()["tiles"][0]

    response = client.get(f"/tilejson.json?url={DATA_DIR}/cog.tif&minzoom=5&maxzoom=12")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json()["tilejson"]
    assert response.json()["minzoom"] == 5
    assert response.json()["maxzoom"] == 12

    response = client.get(
        f"/WMTSCapabilities.xml?url={DATA_DIR}/cog.tif&minzoom=5&maxzoom=12"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/xml"
    meta = parse_img(response.content)
    assert meta["driver"] == "WMTS"
    assert meta["crs"] == "EPSG:3857"

    response = client.get(
        f"/WorldCRS84Quad/WMTSCapabilities.xml?url={DATA_DIR}/cog.tif&minzoom=5&maxzoom=12"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/xml"
    meta = parse_img(response.content)
    assert meta["driver"] == "WMTS"
    assert str(meta["crs"]) == "OGC:CRS84"

    response = client.get(f"/bounds?url={DATA_DIR}/cog.tif")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json()["bounds"]

    response = client.get(f"/info?url={DATA_DIR}/cog.tif")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json()["band_metadata"]

    response = client.get(f"/info.geojson?url={DATA_DIR}/cog.tif")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    assert response.json()["type"] == "Feature"

    response = client.get(
        f"/preview.png?url={DATA_DIR}/cog.tif&rescale=0,1000&max_size=256"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert 256 in (meta["width"], meta["height"])

    response = client.get(
        f"/preview.png?url={DATA_DIR}/cog.tif&rescale=0,1000&max_size=256&height=512&width=512"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert meta["width"] == 512
    assert meta["height"] == 512

    response = client.get(
        f"/preview.png?url={DATA_DIR}/cog.tif&rescale=0,1000&max_size=0&nodata=0"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert meta["width"] == 2658
    assert meta["height"] == 2667

    response = client.get(
        f"/preview.png?url={DATA_DIR}/cog.tif&rescale=0,1000&max_size=0&nodata=0"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    meta = parse_img(response.content)
    assert meta["width"] == 2658
    assert meta["height"] == 2667

    response = client.get(
        f"/preview.tif?url={DATA_DIR}/cog_scale.tif&unscale=True&return_mask=false"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["dtype"] == "float32"
    assert meta["count"] == 1

    response = client.get(
        f"/preview.tif?url={DATA_DIR}/cog_scale.tif&return_mask=false"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["dtype"] == "int16"
    assert meta["count"] == 1

    feature = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [-59.23828124999999, 74.16408546675687],
                    [-59.83154296874999, 73.15680773175981],
                    [-58.73291015624999, 72.88087095711504],
                    [-56.62353515625, 73.06104462497655],
                    [-55.17333984375, 73.41588526207096],
                    [-55.2392578125, 74.09799577518739],
                    [-56.88720703125, 74.2895142503942],
                    [-57.23876953124999, 74.30735341486248],
                    [-59.23828124999999, 74.16408546675687],
                ]
            ],
        },
    }

    feature_collection = {"type": "FeatureCollection", "features": [feature]}

    response = client.post(f"/crop?url={DATA_DIR}/cog.tif", json=feature)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"

    response = client.post(f"/crop.tif?url={DATA_DIR}/cog.tif", json=feature)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["dtype"] == "uint16"
    assert meta["count"] == 2

    response = client.post(f"/crop/100x100.jpeg?url={DATA_DIR}/cog.tif", json=feature)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    meta = parse_img(response.content)
    assert meta["width"] == 100
    assert meta["height"] == 100

    # GET - statistics
    response = client.get(f"/statistics?url={DATA_DIR}/cog.tif&bidx=1&bidx=1&bidx=1")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    resp = response.json()
    assert len(resp) == 1
    assert set(resp["b1"].keys()) == {
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
    assert len(resp["b1"]["histogram"][0]) == 10

    response = client.get(f"/statistics?url={DATA_DIR}/cog.tif&expression=b1*2")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    resp = response.json()
    assert len(resp) == 1
    assert set(resp["b1*2"].keys()) == {
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
        f"/statistics?url={DATA_DIR}/cog.tif&bidx=1&bidx=1&bidx=1&p=4&p=5"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    resp = response.json()
    assert len(resp) == 1
    assert set(resp["b1"].keys()) == {
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
        "percentile_4",
        "percentile_5",
    }

    response = client.get(f"/statistics?url={DATA_DIR}/cog.tif&categorical=true")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    resp = response.json()
    assert len(resp) == 1
    assert set(resp["b1"].keys()) == {
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
    # categories are stored in the histogram
    assert len(resp["b1"]["histogram"][1]) == 15

    response = client.get(
        f"/statistics?url={DATA_DIR}/cog.tif&categorical=true&c=1&c=2&c=3&c=4"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    resp = response.json()
    assert len(resp) == 1
    assert set(resp["b1"].keys()) == {
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
    assert resp["b1"]["histogram"][1] == [1.0, 2.0, 3.0, 4.0]  # categories
    assert resp["b1"]["histogram"][0][3] == 0  # 4.0 is not present in the array

    response = client.get(f"/statistics?url={DATA_DIR}/cog.tif&bidx=1&histogram_bins=3")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    resp = response.json()
    assert len(resp) == 1
    assert len(resp["b1"]["histogram"][0]) == 3

    response = client.get(
        f"/statistics?url={DATA_DIR}/cog.tif&bidx=1&histogram_range=5,10"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    resp = response.json()
    assert len(resp) == 1
    assert min(resp["b1"]["histogram"][1]) == 5.0
    assert max(resp["b1"]["histogram"][1]) == 10.0

    # POST - statistics
    response = client.post(
        f"/statistics?url={DATA_DIR}/cog.tif&bidx=1&bidx=1&bidx=1", json=feature
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    resp = response.json()
    assert resp["type"] == "Feature"
    assert len(resp["properties"]["statistics"]) == 1
    assert set(resp["properties"]["statistics"]["b1"].keys()) == {
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
        "percentile_2",
        "percentile_98",
        "valid_pixels",
        "masked_pixels",
        "valid_percent",
    }

    response = client.post(
        f"/statistics?url={DATA_DIR}/cog.tif&bidx=1&bidx=1&bidx=1",
        json=feature_collection,
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    resp = response.json()
    assert resp["type"] == "FeatureCollection"
    assert len(resp["features"][0]["properties"]["statistics"]) == 1
    assert set(resp["features"][0]["properties"]["statistics"]["b1"].keys()) == {
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
        "percentile_2",
        "percentile_98",
        "valid_pixels",
        "masked_pixels",
        "valid_percent",
    }

    response = client.post(
        f"/statistics?url={DATA_DIR}/cog.tif&categorical=true", json=feature
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    resp = response.json()
    assert resp["type"] == "Feature"
    assert len(resp["properties"]["statistics"]) == 1
    assert set(resp["properties"]["statistics"]["b1"].keys()) == {
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
        "percentile_2",
        "percentile_98",
        "valid_pixels",
        "masked_pixels",
        "valid_percent",
    }
    assert len(resp["properties"]["statistics"]["b1"]["histogram"][1]) == 12

    response = client.post(
        f"/statistics?url={DATA_DIR}/cog.tif&categorical=true&c=1&c=2&c=3&c=4",
        json=feature,
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/geo+json"
    resp = response.json()
    assert resp["type"] == "Feature"
    assert len(resp["properties"]["statistics"]) == 1
    assert set(resp["properties"]["statistics"]["b1"].keys()) == {
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
        "percentile_2",
        "percentile_98",
        "valid_pixels",
        "masked_pixels",
        "valid_percent",
    }
    assert len(resp["properties"]["statistics"]["b1"]["histogram"][0]) == 4
    assert resp["properties"]["statistics"]["b1"]["histogram"][0][3] == 0

    # Test with Algorithm
    response = client.get(f"/preview.tif?url={DATA_DIR}/dem.tif&return_mask=False")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["dtype"] == "float32"
    assert meta["count"] == 1

    response = client.get(
        f"/preview.tif?url={DATA_DIR}/dem.tif&return_mask=False&algorithm=terrarium"
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/tiff; application=geotiff"
    meta = parse_img(response.content)
    assert meta["dtype"] == "uint8"
    assert meta["count"] == 3