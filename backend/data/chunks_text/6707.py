- Defines a middleware function `ep_middleware()` that sets cookies on entry and exit of an endpoint (EP).
- Appends this middleware to the list of EP middlewares using `ep.middlewares`.
- Defines another middleware function `method_middleware()` for a specific RPC method called `probe()`.
- Adds this method middleware to the list of middlewares for the `probe()` method using `@ep.method(...)`.
- Inside the `probe()` method, sets a cookie with the request body as its value and returns it along with a status code of 404.