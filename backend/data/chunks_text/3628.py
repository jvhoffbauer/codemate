- Defines an asynchronous context manager called `lifespan()`.
- Sets a flag in the application's global state (`state`) to indicate that the app has started up when entering the context manager.
- Yields control back to the caller of this function.
- When leaving the context manager, sets another flag in the global state to indicate that the app is shutting down.