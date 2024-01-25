    def _create_schema_update(self) -> Type[SchemaUpdateT]:
        # Set the update fields to the model insfields if not provided
        self.update_fields = self.update_fields or self.model_insfields
        # Exclude certain fields if specified
        exclude = {
            k
            for k, v in ValueItems.merge(self.update_exclude, {}).items()
            if not isinstance(v, (dict, list, set))
        } or {self.pk_name}
        # Filter out any non-model fields from the update fields
        modelfields = self.parser.filter_modelfield(self.update_fields, exclude=exclude)
        # Create the schema using the model fields
        return create_model_by_fields(
            name=f"{self.schema_name_prefix}Update",
            fields=modelfields,
            set_none=True,
        )