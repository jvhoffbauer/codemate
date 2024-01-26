- Imports `pydantic`, creates an instance of `FastAPI`, and defines two endpoints using its decorator syntax.
- Defines a custom UUID subclass called `MyUuid`.
- Uses `vars()` to check if the custom UUID behaves like builtin Python's `uuid.UUID`.
- Tests raising a TypeError when trying to access arbitrary attributes on the custom UUID object.
- Creates a custom Pydantic model called `SomeCustomClass` with a custom UUID field.
- Adds a serialization method to the custom UUID field in order to convert it into a string before sending it over the network (required by FastAPI).
- Makes requests to both endpoints using `TestClient` and checks their responses.