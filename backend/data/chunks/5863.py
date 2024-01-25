    def _create_schema_create(self) -> Type[SchemaCreateT]:
        # Set the create fields to the model insfields if not provided
        self.create_fields = self.create_fields or self.model_insfields
        # Exclude certain fields if specified
        exclude = {
            k
            for k, v in ValueItems.merge(self.create_exclude, {}).items()
            if not isinstance(v, (dict, list, set))
        } or {self.pk_name}
        # Filter out any non-model fields from the create fields
        modelfields = self.parser.filter_modelfield(self.create_fields, exclude=exclude)
        # Create the schema using the model fields
        return create_model_by_fields(
            name=f"{self.schema_name_prefix}Create",
            fields=modelfields,
        )