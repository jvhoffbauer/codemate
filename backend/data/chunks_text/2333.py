- Extracts default values for three parameters (swagger_js_url, swagger_css_url, and swagger_favicon_url) from a function signature using Python's `inspect` module.
- Calls the `get_swagger_ui_html` function with some arguments to generate HTML content containing Swagger UI components.
- Retrieves the generated HTML content and extracts its body text as a string.
- Asserts that the extracted strings contain the previously obtained default parameter values, indicating that they were correctly passed into the HTML generation process.