- Defines a GET route for `"/cookie_example/"`, which takes an optional query parameter called `data`.
- Uses FastAPI's built-in `Cookie` decorator to create a custom cookie with a default value of `None` and an example value of `"cookie1"`.
- Returns the value of the `data` cookie or its default value if it is not present in the request headers.