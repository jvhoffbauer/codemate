- Tests the `/info`, `/info.geojson`, and `/point` endpoints for a COG with NODATA values represented as float32 (NaN) using mocked RasterIO functions. - Verifies that the expected JSON responses are returned with correct nodata information.