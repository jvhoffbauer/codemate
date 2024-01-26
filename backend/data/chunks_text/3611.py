- Uses `pytest.mark.filterwarnings` to ignore a specific DeprecationWarning related to `on_event`.
- Defines an instance of `FastAPI`, registers routes and event listeners for both the application and routers.
- Includes a nested router within another router using `include_router`.
- Asserts that all event listeners are called in the correct order during startup and shutdown phases.
- Makes a request to one of the registered endpoints to ensure proper behavior during runtime.