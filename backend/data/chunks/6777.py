    def openapi(self):
        result = super().openapi()

        if self.fastapi_jsonrpc_components_fine_names and "components" in result:
            self._restore_json_schema_fine_component_names(result)

        for route in self.routes:
            if isinstance(
                route,
                (
                    EntrypointRoute,
                    MethodRoute,
                ),
            ):
                route: Union[EntrypointRoute, MethodRoute]
                for media_type in result["paths"][route.path]:
                    result["paths"][route.path][media_type]["responses"].pop(
                        "default", None
                    )
        return result