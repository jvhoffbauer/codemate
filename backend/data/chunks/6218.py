def create_model_by_model(
    model: Type[BaseModel],
    name: str,
    *,
    include: Set[str] = None,
    exclude: Set[str] = None,
    set_none: bool = False,
    **kwargs,
) -> Type[BaseModel]:
    """Create a new model by the BaseModel."""
    fields = model_fields(model)
    keys = set(fields.keys())
    if include:
        keys &= include
    if exclude:
        keys -= exclude
    fields = {
        name: create_cloned_field(field)
        for name, field in fields.items()
        if name in keys
    }
    return create_model_by_fields(
        name, list(fields.values()), set_none=set_none, **kwargs
    )