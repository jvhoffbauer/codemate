- Adds a new `/viewer` endpoint to the TilerFactory using the `register()` method of the FactoryExtension class. - The `cog_viewer()` function is registered as an endpoint with the GET HTTP method and returns an HTML response generated by the `templates.TemplateResponse()` function. - The viewer page displays three endpoints for accessing tile JSON, metadata (INFO), and statistics data associated with the COG dataset being served by the TilerFactory.