- Defines a `FastAPI` application and creates two endpoints for testing dependencies on `DatasetParams`.
- Uses `TestClient` to make requests to the endpoints with different query parameters, verifying that the expected values are returned by the dependencies.
- Tests for missing data (`nodata`) and unscaled input (`unscale`) using both query parameter and default value.
- Tests for custom resampling method passed as query parameter.