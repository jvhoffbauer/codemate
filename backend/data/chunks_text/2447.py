- Tests the `async_raise` endpoint by making a GET request using the `TestClient`.
- Disables raising server exceptions with `raise_server_exceptions=False`.
- Asserts that the status code is 500 and saves the text for later comparison.
- Saves the current value of `state` dictionary for `/async_raise` key.
- Checks if `/async_raise` is present in `errors` dictionary (which should be empty).
- Clears the `errors` dictionary after checking its contents.