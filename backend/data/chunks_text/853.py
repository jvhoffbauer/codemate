- Defines a function `websocket_route()` that takes two arguments `path` and `name`.
- The returned value is another function called `decorator()`, which accepts a decorated callable (a function with decorators applied).
- Inside `decorator()`, it adds the given `path` and `func` to the router's list of WebSocket routes using the `add_websocket_route()` method from the parent class. Optionally sets the route's name as well.
- Finally, returns the original decorated callable unchanged for chaining purposes.