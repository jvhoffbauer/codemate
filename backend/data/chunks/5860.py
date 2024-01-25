    def _create_schema_filter(self) -> Type[SchemaFilterT]:
        # Get the filter fields from the list filter or select entities
        list_filter = self.list_filter or self._select_entities.values()
        # Filter out the model fields from the filter fields
        modelfields = self.parser.filter_modelfield(list_filter, save_class=(Label,))
        # Modify the modelfields if necessary
        for modelfield in modelfields:
            type_ = annotation_outer_type(modelfield.type_)
            if field_annotation_is_scalar(modelfield.type_) and issubclass(
                type_, (Enum, bool, str)
            ):
                continue
            if PYDANTIC_V2:
                modelfield.field_info.annotation = str
            else:
                modelfield.type_ = str
                modelfield.outer_type_ = str
                modelfield.validators = []
        # Create the schema using the model fields
        return create_model_by_fields(
            name=f"{self.schema_name_prefix}Filter",
            fields=modelfields,
            set_none=True,
        )