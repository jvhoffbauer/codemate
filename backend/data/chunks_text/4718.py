- Sends multiple files using `FastAPI`'s built-in testing client (`TestClient`) to a custom endpoint for handling file uploads (`/files/`)
- Uses temporary directories provided by `pytest` (`tmp_path`) and writes some sample data into two separate files (`path` and `path2`)
- Passes both files to the request body under the same key ('files') using a tuple of tuples syntax in Python 3.9+ (PEP 612)
- Asserts that the server returns an HTTP status code of 200 OK and parses the JSON response containing the sizes of each uploaded file