    def read_item(self, obj: TableModelT) -> SchemaReadT:
        """read database data and parse to schema_read"""
        return parse_obj_to_schema(obj, self.schema_read)