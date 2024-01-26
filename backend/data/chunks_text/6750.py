- Decorates a method with `@ep.method` and specifies that it may raise an instance of `MyError`. - Allows for more specific error handling in the caller's try/except block, as opposed to catching generic exceptions like `Exception` or `BaseException`. - Helps improve code readability by making intent clearer through explicit error types.