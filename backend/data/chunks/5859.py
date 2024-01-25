    def _create_schema_list(self) -> Type[SchemaListT]:
        # Get the model fields from the select entities
        modelfields = self.parser.filter_modelfield(
            self._select_entities.values(),
            save_class=(
                Label,
                ModelField,
            ),
        )
        # Create the schema using the model fields
        return create_model_by_fields(
            name=f"{self.schema_name_prefix}List",
            fields=modelfields,
            set_none=True,
            extra="allow",
        )