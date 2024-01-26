- Receives a POST request with a body containing a YAML document representing an item to be created
- Converts the request body from bytes to Python object using `aiohttp.web.Request.body()` and `yaml.safe_load()`
- Attempts to validate the parsed YAML against a schema defined by Pydantic's `Item.parse_obj()`, raising a `ValidationError` if validation fails
- Returns the validated item object in response to the client