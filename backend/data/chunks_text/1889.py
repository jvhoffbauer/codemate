- Defines a new asynchronous function called `custom_route_handler`.
- Accepts an instance of `Request` as its argument and returns an instance of `Response`.
- Creates a new object from the `GzipRequest` class with the scope and receive method of the incoming request. This compresses the response using gzip compression.
- Calls the existing route handler (stored in `original_route_handler`) with the modified request object.