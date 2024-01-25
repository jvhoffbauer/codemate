def get_insfield_by_key(
    table_model: Type[TableModelT], key: str
) -> Optional[InstrumentedAttribute]:
    """Get the field of the model according to the alias"""
    for insfield in table_model.__dict__.values():
        if isinstance(insfield, InstrumentedAttribute) and insfield.key == key:
            return insfield
    return None