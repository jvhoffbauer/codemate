    def register(self, factory: BaseTilerFactory):
        """Register endpoint to the tiler factory."""

        @factory.router.get("/viewer", response_class=HTMLResponse)
        def stac_viewer(request: Request):
            """STAC Viewer."""
            return templates.TemplateResponse(
                name="stac_index.html",
                context={
                    "request": request,
                    "tilejson_endpoint": factory.url_for(request, "tilejson"),
                    "info_endpoint": factory.url_for(request, "info"),
                    "statistics_endpoint": factory.url_for(request, "asset_statistics"),
                },
                media_type="text/html",
            )