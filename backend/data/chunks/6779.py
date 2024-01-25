    def openrpc(self):
        if self.openrpc_schema is None:
            self.openrpc_schema = self.get_openrpc()

        if (
            self.fastapi_jsonrpc_components_fine_names
            and "components" in self.openrpc_schema
        ):
            self._restore_json_schema_fine_component_names(self.openrpc_schema)

        return self.openrpc_schema