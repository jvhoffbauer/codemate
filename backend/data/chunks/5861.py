    def _create_schema_read(self) -> Optional[Type[SchemaReadT]]:
        if not self.read_fields:
            return None
        # Filter out any non-model fields from the read fields
        modelfields = self.parser.filter_modelfield(self.read_fields)
        # Create the schema using the model fields
        return create_model_by_fields(
            name=f"{self.schema_name_prefix}Read",
            fields=modelfields,
            orm_mode=True,
        )