- Tests the `TMSFactory` class to ensure it creates a router with two endpoints for listing and retrieving tile matrix sets.
- Includes the created router in a FastAPI application and tests GET requests for both endpoint paths using a `TestClient`.
- Verifies that the correct number of default tile matrix sets are returned when no specific set is requested.
- Retrieves a specific tile matrix set by ID and checks its properties.
- Creates an instance of `TMSFactory` with custom supported tile matrix sets and includes the resulting router in another FastAPI application.
- Makes GET requests for both endpoint paths again, this time verifying that only the specified tile matrix sets are available.
- Attempts to retrieve a non-existent tile matrix set and confirms a 422 status code is returned.