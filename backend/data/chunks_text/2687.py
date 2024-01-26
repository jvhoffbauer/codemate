- This endpoint returns a `User` object with name "John" and surname "Doe".
- The `response_model` parameter is set to `None`, indicating that no specific JSON schema will be used for serialization/deserialization of the returned data.
- However, since we're still returning an instance of our custom `User` model, FastAPI will automatically use its own built-in serializer to convert it into JSON format.