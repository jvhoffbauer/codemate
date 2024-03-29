- Creates a new instance of `AsyncClient` using the provided FastAPI application and sets its base URL to "http://test".
- Uses the `LifespanManager` from FastAPI to manage the lifecycle of the `AsyncClient`.
- Yields the `AsyncClient` for use in other tests within this fixture.