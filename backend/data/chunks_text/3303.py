- Defines a GET request handler for the root URL (/) using FastAPI's `@app.get()` decorator.
- Uses dependency injection to automatically provide an integer value named 'foo', which is obtained from another function called 'dep'. This allows us to avoid passing arguments explicitly in the route definition and makes our code more reusable and testable.
- The `Depends()` function takes care of resolving the dependencies at runtime by calling their respective functions with appropriate arguments if needed. In this case, we are simply forwarding the argument to 'dep' without any modifications.