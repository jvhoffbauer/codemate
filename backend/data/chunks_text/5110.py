- This function named `cog_viewer()` returns a HTML response using Flask's built-in template engine (Jinja2) with the file name 'cog_index.html'.
- The context dictionary passed to the template contains variables for the current HTTP request object ('request'), URL endpoints for accessing TileJSON, INFO and STATISTICS resources of this COG dataset.
- The returned value is an instance of TemplateResponse class which specifies that it should be rendered as text/HTML content type.