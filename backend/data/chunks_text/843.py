- This function generates an HTML response for the Swagger UI page.
- It retrieves the base URL of the application and combines it with the OpenAPI URL to create a complete URL for the API documentation.
- If OAuth2 authentication is enabled, this function also creates a redirect URL for the authorization server.
- The `get_swagger_ui_html()` function from FastAPI's built-in SwaggerUI plugin is called with various parameters that customize the appearance and behavior of the UI. These include the OpenAPI URL, the title of the app, the OAuth2 redirect URL (if present), and some additional configuration options provided by the user.