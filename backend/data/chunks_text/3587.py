- Defines a Pydantic model for a query parameter called `data`, with a default value of `None`.
- Specifies that the `default` value should be used if no value is provided in the request URL.
- Provides two example values (`"json_schema_cookie1"` and `"json_schema_cookie2"`) to help users understand how to format their input.
- Includes OpenAPI documentation for two cookies ("Cookie One" and "Cookie Two"), each with a summary, description, and value. This allows developers using tools like Swagger or Postman to easily test the endpoint with different cookie values.