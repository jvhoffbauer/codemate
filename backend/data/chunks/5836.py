def parse_obj_to_schema(
    obj: TableModelT, schema: Type[SchemaT], refresh: bool = False
) -> SchemaT:
    """parse obj to schema"""
    if refresh:
        object_session(obj).refresh(obj)
    orm_mode = model_config_attr(schema, "orm_mode", False) or model_config_attr(
        schema, "from_attributes", False
    )
    parse = schema.from_orm if orm_mode else schema.parse_obj
    return parse(obj)