- This function is a FastAPI endpoint with the path `/deaths`.
- It uses the `@V1.get()` decorator to define an HTTP GET request handler for version V1 of the API.
- The function retrieves data on total deaths using the `get_category()` asynchronous function and returns it in JSON format.