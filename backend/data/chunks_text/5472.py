- Tests the `/info` and `/info.geojson` endpoints using a mocked RasterIO library to retrieve metadata from a COG at a URL. - Verifies that the expected metadata is returned in JSON format for both endpoints, including bounds, band descriptions, data type, color interpolation, and nodata value (which defaults to None). - Confirms that the GeoJSON output includes geometry information as well as the same metadata fields.