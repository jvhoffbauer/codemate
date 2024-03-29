- Defines a GET request for the `/path_example` endpoint with an optional query parameter named `item_id`.
- Uses FastAPI's built-in `Path` class to parse and validate the `item_id` argument, which can be used as a default value or required using the `title=...` keyword argument (not shown here).
- Returns the parsed `item_id` value as the response body.