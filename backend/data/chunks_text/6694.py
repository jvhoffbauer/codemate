- Defines a middleware function `ep_middleware()` that modifies requests and responses using global variables `_calls` and `ep_middleware_var`. - Sets a value in `ep_middleware_var` before executing the request handler. - Appends an entry to a list associated with the request ID in `_calls`, containing metadata about the request's status and any exceptions encountered during execution. - Yields control back to the request handler, allowing it to execute normally. - After the request handler completes, appends another entry to the same list for the response, again including metadata about its status and any exceptions.