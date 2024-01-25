    def _create_schema_create(self) -> Type[SchemaCreateT]:
        return create_model_by_model(
            self.schema_model,
            f"{self.schema_name_prefix}Create",
            exclude={self.pk_name},
        )