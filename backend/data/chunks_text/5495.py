- Tests the `GET /mosaicjson` and `GET /mosaicjson/` endpoints for retrieving a mosaic JSON file with URL parameter 'MOSAICJSON_FILE' using Flask application context (`app`)
- Verifies that both requests return HTTP status code 200 OK and successfully parse the returned JSON data into a `MosaicJSON` object