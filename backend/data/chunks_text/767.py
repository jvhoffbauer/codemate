- Defines an asynchronous context manager using `@asynccontextmanager`.
- Initializes a connection pool to Redis with maximum connections of 10 and decodes responses.
- Sets the global variable `redis.redis_client` to the initialized Redis client for future use in the application.
- Yields control back to the caller, allowing them to continue executing their async function or coroutine within this context.
- Disconnects from the Redis server during shutdown (only in production environments).