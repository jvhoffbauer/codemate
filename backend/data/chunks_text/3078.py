- Defines a base model `PersonBase`, which has fields for `name` and `lastname`.
- Creates derived models `Person` and `PersonCreate` from `PersonBase`.
- Adds a custom property `full_name` to `Person`.
- Sets up configuration options for each model using `ConfigDict`.
- Registers an endpoint with `FastAPI` that accepts a `PersonCreate` object as input and returns a `PersonRead` object as output.
- Uses `TestClient` to make a POST request to the endpoint with sample data.
- Asserts that the expected status code (200), JSON body, and values are returned by the server.