- Defines a function `probe` that takes an endpoint object (`ep`) as input and returns another endpoint object with a new method called `probe`.
- The new method, also named `probe`, is decorated with the `@ep.method()` decorator to indicate it's a REST API endpoint.
- It accepts a single argument `jsonrpc_request_id` of type `int` which is retrieved using the `Depends` utility from the `get_jsonrpc_request_id` function. This allows us to pass request context between functions in FastAPI applications.
- The method simply returns the value of `jsonrpc_request_id`.