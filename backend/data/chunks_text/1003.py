- This function is an asynchronous callable object that takes a `Request` instance and returns an optional string.
- It checks for the presence of an "Authorization" header in the request headers. If it's not present, it raises a `HTTPException` with a 403 Forbidden status code and a message indicating that authentication is required (unless auto error handling is disabled). Otherwise, it simply returns the value of the Authorization header.