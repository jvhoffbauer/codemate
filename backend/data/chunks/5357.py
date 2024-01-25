        def cog_viewer(request: Request):
            """COG Viewer."""
            return templates.TemplateResponse(
                name="cog_index.html",
                context={
                    "request": request,
                    "tilejson_endpoint": factory.url_for(request, "tilejson"),
                    "info_endpoint": factory.url_for(request, "info"),
                    "statistics_endpoint": factory.url_for(request, "statistics"),
                },
                media_type="text/html",
            )