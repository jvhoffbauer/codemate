- Tests that raising an exception when trying to define defaults for path parameters using FastAPI's `Path()` decorator. The error message should contain the expected string.
- Tests that raising an exception when trying to define defaults for query parameters using FastAPI's `Query()` decorator inside an `Annotated` object. The error message should also contain the expected string.