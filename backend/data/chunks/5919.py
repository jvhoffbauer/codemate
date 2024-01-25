    def _create_schema_update(self) -> Type[SchemaUpdateT]:
        return create_model_by_model(
            self.schema_model,
            f"{self.schema_name_prefix}Update",
            exclude={self.pk_name},
            set_none=True,
        )