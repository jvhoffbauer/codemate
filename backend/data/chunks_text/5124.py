- Tests the `cogViewerExtension` class by creating two instances of `TilerFactory`, one without and one with the extension added, and checking that there is an additional route in the latter's router.
- Demonstrates how to include the extended router in a FastAPI application using the `include_router` function.
- Makes a GET request to the new viewer route created by the extension and checks its status code and content type.