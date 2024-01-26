- Tests if a GET request to `/path/param-gt0/{value}` with `{value}=0.05` returns status code 200 and value in JSON format
- Verifies that the path parameter `{value}` is greater than zero (implicitly tested by the route definition)
- Asserts that the returned JSON value matches the expected one, which is `0.05`