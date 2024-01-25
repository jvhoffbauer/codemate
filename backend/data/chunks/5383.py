def test_wmsExtension_GetMap():
    """Test wmsValidateExtension class."""
    tiler_plus_wms = TilerFactory(extensions=[wmsExtension()])

    app = FastAPI()
    app.include_router(tiler_plus_wms.router)
    with TestClient(app) as client:
        response = client.get(
            "/wms",
            params={
                "VERSION": "1.3.0",
                "REQUEST": "GetMap",
                "LAYERS": cog,
            },
        )
        assert response.status_code == 400
        assert "Missing 'GetMap' parameters: " in response.text

        response = client.get(
            "/wms",
            params={
                "VERSION": "1.3.0",
                "REQUEST": "GetMap",
                "LAYERS": cog,
                "BBOX": "373185.0,8019284.949381611,639014.9492102272,8286015.0",
                "CRS": "EPSG:32621",
                "WIDTH": 334,
                "HEIGHT": 333,
                "FORMAT": "image/png",
                "TRANSPARENT": False,
            },
        )
        assert response.status_code == 200
        meta = parse_img(response.content)
        assert meta["driver"] == "PNG"
        assert meta["width"] == 334
        assert meta["height"] == 333
        assert meta["count"] == 1

        response = client.get(
            "/wms",
            params={
                "VERSION": "1.3.0",
                "REQUEST": "GetMap",
                "LAYERS": cog,
                "BBOX": "373185.0,8019284.949381611,639014.9492102272,8286015.0",
                "CRS": "EPSG:32621",
                "WIDTH": 334,
                "HEIGHT": 333,
                "FORMAT": "image/png",
                "TRANSPARENT": True,
            },
        )
        assert response.status_code == 200
        meta = parse_img(response.content)
        assert meta["driver"] == "PNG"
        assert meta["width"] == 334
        assert meta["height"] == 333
        assert meta["count"] == 2

        response = client.get(
            "/wms",
            params={
                "VERSION": "1.3.0",
                "REQUEST": "GetMap",
                "LAYERS": cog,
                "BBOX": "373185.0,8019284.949381611,639014.9492102272,8286015.0",
                "SRS": "EPSG:32621",
                "WIDTH": 334,
                "HEIGHT": 333,
                "FORMAT": "image/tiff; application=geotiff",
            },
        )
        assert response.status_code == 200
        meta = parse_img(response.content)
        assert meta["crs"] == CRS.from_epsg(32621)

        response = client.get(
            "/wms",
            params={
                "VERSION": "1.3.0",
                "REQUEST": "GetMap",
                "LAYERS": cog,
                "BBOX": "373185.0,8019284.949381611,639014.9492102272,8286015.0",
                "CRS": "EPSG:32621",
                "WIDTH": 334,
                "HEIGHT": 333,
                "FORMAT": "image/tiff; application=geotiff",
            },
        )
        assert response.status_code == 200
        meta = parse_img(response.content)
        assert meta["driver"] == "GTiff"
        assert meta["width"] == 334
        assert meta["height"] == 333
        assert meta["crs"] == CRS.from_epsg(32621)

        response = client.get(
            "/wms",
            params={
                "VERSION": "1.3.0",
                "REQUEST": "GetMap",
                "LAYERS": cog,
                "BBOX": "373185.0,8019284.949381611,639014.9492102272,8286015.0",
                "CRS": "",
                "WIDTH": 334,
                "HEIGHT": 333,
                "FORMAT": "image/png",
                "TRANSPARENT": True,
            },
        )
        assert response.status_code == 400
        assert "Invalid 'CRS' parameter" in response.text

        response = client.get(
            "/wms",
            params={
                "VERSION": "1.3.1",
                "REQUEST": "GetMap",
                "LAYERS": cog,
                "BBOX": "373185.0,8019284.949381611,639014.9492102272,8286015.0",
                "CRS": "EPSG:32621",
                "WIDTH": 334,
                "HEIGHT": 333,
                "FORMAT": "image/png",
            },
        )
        assert response.status_code == 400
        assert "Invalid 'VERSION' parameter" in response.text

        response = client.get(
            "/wms",
            params={
                "VERSION": "1.3.0",
                "REQUEST": "GetMap",
                "LAYERS": cog,
                "BBOX": "373185.0,8019284.949381611,639014.9492102272,8286015.0",
                "WIDTH": 334,
                "HEIGHT": 333,
                "FORMAT": "image/png",
            },
        )
        assert response.status_code == 400
        assert "Missing 'CRS' or 'SRS parameters." in response.text

        response = client.get(
            "/wms",
            params={
                "VERSION": "1.3.0",
                "REQUEST": "GetMap",
                "LAYERS": cog,
                "BBOX": "373185.0,373185.0,8019284.949381611,639014.9492102272,8286015.0",
                "CRS": "EPSG:32621",
                "WIDTH": 334,
                "HEIGHT": 333,
                "FORMAT": "image/png",
            },
        )
        assert response.status_code == 400
        assert "Invalid 'BBOX' parameters" in response.text

        # 1.3.0 needs inverted X,Y coordinates for EPSG:4326
        response = client.get(
            "/wms",
            params={
                "VERSION": "1.3.0",
                "REQUEST": "GetMap",
                "LAYERS": cog,
                "BBOX": "72.22979795551834,-61.28762442711404,74.66298001264106,-52.301598718454485",
                "CRS": "EPSG:4326",
                "WIDTH": 334,
                "HEIGHT": 333,
                "FORMAT": "image/tiff; application=geotiff",
            },
        )
        assert response.status_code == 200
        meta = parse_img(response.content)
        assert meta["crs"] == CRS.from_epsg(4326)
        assert meta["bounds"] == [
            -61.28762442711404,
            72.22979795551834,
            -52.301598718454485,
            74.66298001264106,
        ]

        response = client.get(
            "/wms",
            params={
                "VERSION": "1.1.1",
                "REQUEST": "GetMap",
                "LAYERS": cog,
                "BBOX": "-61.28762442711404,72.22979795551834,-52.301598718454485,74.66298001264106",
                "CRS": "EPSG:4326",
                "WIDTH": 334,
                "HEIGHT": 333,
                "FORMAT": "image/tiff; application=geotiff",
            },
        )
        assert response.status_code == 200
        meta = parse_img(response.content)
        assert meta["crs"] == CRS.from_epsg(4326)
        assert meta["bounds"] == [
            -61.28762442711404,
            72.22979795551834,
            -52.301598718454485,
            74.66298001264106,
        ]

        response = client.get(
            "/wms",
            params={
                "VERSION": "1.3.0",
                "REQUEST": "GetMap",
                "LAYERS": cog,
                "BBOX": "-61.28762442711404,72.22979795551834,-52.301598718454485,74.66298001264106",
                "CRS": "CRS:84",
                "WIDTH": 334,
                "HEIGHT": 333,
                "FORMAT": "image/tiff; application=geotiff",
            },
        )
        assert response.status_code == 200
        meta = parse_img(response.content)
        assert meta["crs"] == CRS.from_epsg(4326)
        assert meta["bounds"] == [
            -61.28762442711404,
            72.22979795551834,
            -52.301598718454485,
            74.66298001264106,
        ]