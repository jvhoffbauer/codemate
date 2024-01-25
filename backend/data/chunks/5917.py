    def _create_schema_filter(self) -> Type[SchemaFilterT]:
        return create_model_by_model(
            self.schema_list, f"{self.schema_name_prefix}Filter", set_none=True
        )