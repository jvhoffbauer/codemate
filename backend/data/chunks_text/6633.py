- Defines an asynchronous middleware function `ep_middleware` that takes a `JsonRpcContext` object as input and returns nothing (yields).
- Retrieves authentication credentials from the HTTP request using another function called `security`.
- Applies some additional authorization logic to the retrieved credentials using another function called `auth_user`.
- Stores the updated credentials in a global variable named `credentials_var`, which is reset at the end of the middleware execution to restore its original value.