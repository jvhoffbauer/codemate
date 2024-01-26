- Defines a GET route with path `/query/param-required`.
- Uses FastAPI's built-in Query class to parse and validate query parameters, in this case named "query".
- Returns a string concatenating fixed text ("foo bar ") and the parsed query parameter value (accessed via the Query object).