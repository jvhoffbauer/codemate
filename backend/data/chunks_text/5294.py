- Defines a GET request for the `/route1` endpoint using FastAPI's decorator syntax (`@app.get`)
- Includes a query parameter named `value`, which is required and can be passed as part of the URL query string (`Query(...)`)
- Returns a JSON response with a key-value pair containing the provided `value`