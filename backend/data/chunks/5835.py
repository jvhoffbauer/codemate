def get_modelfield_by_alias(
    table_model: Type[TableModelT], alias: str
) -> Optional[ModelField]:
    """Get the field of the model according to the alias"""
    fields = TableModelParser.get_table_model_fields(table_model).values()
    for field in fields:
        if field.alias == alias:
            return field
    return None