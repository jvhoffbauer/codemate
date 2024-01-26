- Defines a GET route with path `/query/int/optional`.
- Uses FastAPI's `Optional` type hint to make the `query` parameter optional and set its default value to `None`.
- Returns either a static string ("foo bar") or a formatted string that includes the value of the `query` parameter, depending on whether it was provided in the request.