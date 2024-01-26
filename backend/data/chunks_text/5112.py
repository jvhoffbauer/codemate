- Registers an endpoint for a STAC viewer using the given `BaseTilerFactory`.
- The viewer is accessed at the URL `/viewer`, and returns an HTML response generated by the `templates.TemplateResponse()` function.
- The viewer's context includes the current request object, as well as URL endpoints for accessing tile JSON, metadata (INFO), and asset statistics data provided by the `BaseTilerFactory`.