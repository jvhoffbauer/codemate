    def list_item(self, values: Dict[str, Any]) -> SchemaListT:
        """Parse the database data query result dictionary into schema_list."""
        return self.schema_list.parse_obj(values)