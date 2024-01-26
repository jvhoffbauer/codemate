- Defines an asynchronous function `verify_token` that takes a header named 'x_token' as input and sets its default value to be obtained from the request headers using FastAPI's built-in decorator `Header`.
- Checks whether the value of the 'x_token' header is equal to a hardcoded string ("fake-super-secret-token"). If not, raises a customized HTTP exception with status code 400 (Bad Request) and error message "X-Token header invalid".