- Sets environment variable `GDAL_DISABLE_READDIR_ON_OPEN` to a custom value using `monkeypatch`.
- Creates an instance of `FastAPI` and defines routes for handling requests.
- Defines a function `f` that retrieves the value of `GDAL_DISABLE_READDIR_ON_OPEN` using `rasterio.Env`.
- Registers the defined routes under a `APIRouter` object called `router`.
- Includes the registered routes in the main application instance created by `FastAPI`.
- Uses `TestClient` to make HTTP requests against the running server and tests if the expected values are returned based on different scenarios (sync vs async).