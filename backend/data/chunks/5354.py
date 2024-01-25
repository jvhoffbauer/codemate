@dataclass
class cogViewerExtension(FactoryExtension):
    """Add /viewer endpoint to the TilerFactory."""

    def register(self, factory: BaseTilerFactory):
        """Register endpoint to the tiler factory."""

        @factory.router.get("/viewer", response_class=HTMLResponse)
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